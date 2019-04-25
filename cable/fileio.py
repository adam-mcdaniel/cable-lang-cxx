from os import system
from shutil import copytree as copy, rmtree as remove
from constants import SCRIPT_PREFIX, SCRIPT_SUFFIX, STD_DIR, CABLE_DIR


def write_main(path, includes=[], script=""):
    with open(path, "w") as f:
        for include in includes:
            f.write(include)
        f.write(SCRIPT_PREFIX)
        f.write(script)
        f.write(SCRIPT_SUFFIX)


def copy_std_to_dir(path):
    try:
        remove(path + "/std")
        remove(path + "/cable")
    except:
        pass
    copy(STD_DIR, path + "/std")
    copy(CABLE_DIR, path + "/cable")


def build(dir):
    system(
        "g++ {dir}/main.cpp -std=c++17 -o {dir}/bin".format(
            dir=dir
        )
    )