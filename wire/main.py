import click
from os import system
from fileio import make_project, update_project
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
    system("./cable compile src/main.cb")
    custom_info("Build complete.")
    

@main.command()
def run():
    "Builds a cablelang project"
    custom_info("Building...")
    system("./cable compile src/main.cb")
    custom_info("Build complete.")
    system("./target/bin")


@main.command()
@click.argument('path')
def update(path):
    "Updates a cablelang project's dependencies and binaries"
    custom_info("Updating project's std library and cablelang deps...")
    update_project(path)
    custom_info("Updated project.")

    
if __name__ == "__main__":
    main()