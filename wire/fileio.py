from os import system
from os.path import exists, isdir, relpath
from shutil import copytree as copy, rmtree as remove
from constants import PROJECT_DIR
from error import custom_error


def make_project(project_name):
    path = relpath(project_name)

    if not isdir(path):
        try:
            remove(path)
        except:
            pass
        copy(PROJECT_DIR, path)
    else:
        custom_error("Project already exists")
