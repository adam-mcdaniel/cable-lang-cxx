import click
from os import mkdir
from sys import argv as cmd_args
from error import custom_error, custom_info
from compiler import Compiler
from constants import OUTPUT_DIR
from fileio import copy_std_to_dir, build_debug, build_release


__version__ = "0.3.0"
__author__ = "Adam McDaniel"
__improvements__ = [
    "v0.2.2 - Added for loops",
    "v0.2.2 - Added +=, -=, *=, /= operators",
    "v0.2.3 - Added support for compiling in arbitrary locations",
    "v0.3.0 - Added support for if statements",
    "v0.3.1 - Added support for getting types as strings",
    "v0.3.2 - Added debug and release modes",
]


@click.group()
def main():
    """
    The compiler for the cablelang programming language.
    """
    pass


@main.command()
def info():
    "Displays info on cable compiler"
    custom_info('Cable compiler v{}'.format(__version__))
    for improvement in __improvements__:
        custom_info(improvement)


@main.command()
@click.argument('input_file')
@click.option('--output-dir', '-o', default=OUTPUT_DIR, help='The output directory of the compiled cablelang script.')
def compile(input_file, output_dir):
    "Compile a cablelang script in debug mode"
    try: mkdir(output_dir)
    except: pass

    copy_std_to_dir(output_dir)
    c = Compiler(input_file, output_dir + '/main.cpp')
    c.compile()
    c.write()
    build_debug(output_dir)


@main.command()
@click.argument('input_file')
@click.option('--output-dir', '-o', default=OUTPUT_DIR, help='The output directory of the compiled cablelang script.')
def release(input_file, output_dir):
    "Compile a cablelang script in release mode"
    try: mkdir(output_dir)
    except: pass

    copy_std_to_dir(output_dir)
    c = Compiler(input_file, output_dir + '/main.cpp')
    c.compile()
    c.write()
    build_release(output_dir)


if __name__ == "__main__":
    main()