from sys import argv
from os.path import relpath, dirname
from pathlib import Path


# For local usage
# BASEDIR = dirname(argv[0])

# For global usage
HOME = str(Path.home())
BASEDIR = HOME + "/cablelang/bin"

PROJECT_DIR = BASEDIR + "/project"