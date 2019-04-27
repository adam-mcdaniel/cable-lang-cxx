from os.path import exists, relpath, dirname
from fileio import write_main, copy_std_to_dir
from lark import Lark, Transformer
from parser import CableLangCXXTree, includes
from error import pretty_error_message, custom_error
from constants import GRAMMAR


class Compiler:
    def __init__(self, input_path, output_path):
        self.input_path = relpath(input_path)
        self.output_path = relpath(output_path)
        self.output = None

    # Compiles the script from the input file
    def compile(self):
        if exists(self.input_path):
            self.output = compile_text(
                open(self.input_path).read(),
                dirname(self.input_path)
                )
        else:
            custom_error(
                "Path '{}' does not exist".format(self.input_path)
                )
    
    # Writes the output of the compiled script
    def write(self):
        if self.output:
            if not self.output.has_errors():
                self.output.write(self.output_path)
            else:
                self.output.error_check()


class CompiledScript:
    def __init__(self, script="", includes=[], imports=[], error=""):
        self.script = script
        self.includes = includes
        self.imports = imports
        self.error = error

    # Does the script have an error?
    def has_errors(self): return self.error != ""

    # Write the compiled cablelang script to the directory
    def write(self, path):
        write_main(path, self.includes, self.script)

    # Print error messages
    def error_check(self):
        pretty_error_message(self.error)


def compile_text(text, directory):
    try:
        script = CableLangCXXTree(directory).transform(
                    Lark(
                        GRAMMAR,
                        start='block',
                        parser='lalr',
                        lexer='standard'
                    ).parse(text)
                )

        return CompiledScript(script=script, includes=includes)
    except Exception as e:
        return CompiledScript(error=e)
