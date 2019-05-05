from os import system
from glob import glob
from os.path import basename
from shutil import copytree as copy, rmtree as remove
from constants import SCRIPT_PREFIX, SCRIPT_SUFFIX, STD_DIR, CABLE_DIR, RESOURCES_DIR


def write_main(path, includes=[], script=""):
    with open(path, "w") as f:
        for include in includes:
            f.write(include)
        f.write(SCRIPT_PREFIX)
        f.write(script)
        f.write(SCRIPT_SUFFIX)


def copy_std_to_dir(path):
    try: remove(path)
    except: pass
    try: mkdir(path)
    except: pass

    for name in glob(RESOURCES_DIR + "/*"):
        copy(name, path + "/" + basename(name))


def build_debug(dir):
    system(
        "g++ {dir}/main.cpp -O0 -std=c++17 -o {dir}/bin".format(
            dir=dir
        )
    )


def build_release(dir):
    system(
        "g++ {dir}/main.cpp -O3 -std=c++17 -o {dir}/bin".format(
            dir=dir
        )
    )