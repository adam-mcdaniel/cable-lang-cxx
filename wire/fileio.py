from os import system, remove
from os.path import exists, isdir, relpath
from shutil import copytree as copy, rmtree as rmdir, copy2 as copyfile
from constants import PROJECT_DIR
from error import custom_error


def rm(path):
    try: rmdir(path)
    except: pass
    try: remove(path)
    except: pass



def make_project(project_name):
    path = relpath(project_name)

    if not isdir(path):
        try:
            rm(path)
        except:
            pass
        copy(PROJECT_DIR, path)
    else:
        custom_error("Project already exists")


def update_project(project_name):
    path = relpath(project_name)

    rm(path + "/include/cable")
    rm(path + "/include/std")
    copy(PROJECT_DIR + "/include/std", path + "/include/std")
    copy(PROJECT_DIR + "/include/cable", path + "/include/cable")
    rm(path + "/cable")
    copyfile(PROJECT_DIR + "/cable", path + "/cable")
