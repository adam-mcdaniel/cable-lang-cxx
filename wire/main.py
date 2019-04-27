import click
from os import system
from fileio import make_project, update_project
from error import custom_info


__version__ = "0.1.4"
__author__ = "Adam McDaniel"
__improvements__ = [
    "Added support for updating multiple projects at once"
]


@click.group()
def main():
    """
    The package manager for the cablelang programming language
    """
    pass


@main.command()
def info():
    "Displays info on wire package manager"
    custom_info('Wire project manager v{}'.format(__version__))
    for improvement in __improvements__:
        custom_info(improvement)


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
@click.argument('paths', nargs=-1)
def update(paths):
    "Updates one or more cablelang projects' dependencies and binaries"
    for path in paths:
        custom_info("Updating project's std library and cablelang deps...")
        update_project(path)
        custom_info("Updated project.")

    
if __name__ == "__main__":
    main()