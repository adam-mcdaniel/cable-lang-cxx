from sys import argv
from os.path import relpath, dirname


SCRIPT_PREFIX = """#include "cable/cable.cpp"

const Fn print_fn = Fn([](Value printed_objects) {
    for (int i=0; i < printed_objects.len().get_i32().unwrap(); i++) {
        cout << printed_objects[i];
    }
    return Value();
});

const Fn println_fn = Fn([](Value printed_objects) {
    for (int i=0; i < printed_objects.len().get_i32().unwrap(); i++) {
        cout << printed_objects[i];
    }
    cout << endl;
    return Value();
});


int main() {
    auto print = Value(print_fn);
    auto println = Value(println_fn);
"""

SCRIPT_SUFFIX = "\n\nreturn 0;\n}"

BASEDIR = dirname(argv[0])

OUTPUT_DIR = relpath("target/")
RESOURCES_DIR = BASEDIR + "/resources/"

STD_DIR = RESOURCES_DIR + "std/"
CABLE_DIR = RESOURCES_DIR + "cable/"
GRAMMAR_PATH = RESOURCES_DIR + "cablelang.lark"