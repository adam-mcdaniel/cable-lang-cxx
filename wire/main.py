import click

__author__ = "Adam McDaniel"


@click.group()
def main():
    """
    The package manager for the cablelang programming language
    """
    pass


@main.command()
@click.argument('project')
def new(project): pass

    
if __name__ == "__main__":
    main()