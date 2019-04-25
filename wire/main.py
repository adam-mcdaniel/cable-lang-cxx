import click
from subprocess import call
from fileio import make_project
from error import custom_info
__author__ = "Adam McDaniel"


@click.group()
def main():
    """
    The package manager for the cablelang programming language
    """
    pass


@main.command()
@click.argument('project_name')
def new(project_name):
    "Creates a new cablelang project"
    make_project(project_name)
    custom_info("Created project '{}'".format(project_name))


@main.command()
def build():
    "Builds a cablelang project"
    custom_info("Building...")
    call(["./cable", "compile", "src/main.cb"])
    custom_info("Build complete.")
    

@main.command()
def run():
    "Builds a cablelang project"
    info("Building...")
    custom_info(["./cable", "compile", "src/main.cb"])
    info("Build complete.")
    custom_info(["./target/bin"])

    
if __name__ == "__main__":
    main()