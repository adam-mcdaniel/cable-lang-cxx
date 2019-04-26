import click
from os import mkdir
from sys import argv as cmd_args
from error import custom_error, custom_info
from compiler import Compiler
from constants import OUTPUT_DIR
from fileio import copy_std_to_dir, build

__version__ = "0.1.1"
__author__ = "Adam McDaniel"


@click.group()
def main():
    """
    The compiler for the cablelang programming language.
    """
    pass


@main.command()
def info():
    "Displays info on wire package manager"
    custom_info('Cable compiler v{}'.format(__version__))


@main.command()
@click.argument('input_file')
@click.option('--output-dir', '-o', default=OUTPUT_DIR, help='The output directory of the compiled cablelang script.')
def compile(input_file, output_dir):
    "Compile a cablelang script"
    try: mkdir(output_dir)
    except: pass

    copy_std_to_dir(output_dir)
    c = Compiler(input_file, output_dir + '/main.cpp')
    c.compile()
    c.write()
    build(output_dir)


if __name__ == "__main__":
    main()