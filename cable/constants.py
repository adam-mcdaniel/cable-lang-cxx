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


GRAMMAR = r'''
//start: (instruction | include | import_)+
//?block: (instruction | include | import_)+
start: (instruction | include)+
?block: (instruction | include)+

include: "include" STRING
//import_: "import" NAME

instruction: while
            | expr ";"
            | retval

?expr: assignment
    | class_def
    | conditional
    | value
    | "(" expr ")" -> wrapped_expr
    | math

eq: expr "==" expr
    | expr "is" expr
noteq: expr "!=" expr
not_: "not" expr
and_: expr "and" expr
or_: expr "or" expr
add: expr "+" expr
subtract: expr "-" expr
multiply: expr "*" expr
divide: expr "/" expr
mod: expr "%" expr
greater: expr ">" expr
less: expr "<" expr
greatereq: expr ">=" expr
lesseq: expr "<=" expr

?math: add
    | subtract
    | multiply
    | divide
    | mod
    | eq
    | noteq
    | not_
    | and_
    | or_
    | greatereq
    | lesseq
    | greater
    | less

member_def: write -> member_def
            | variable "=" expr -> member_def
class_def: "class" variable "{" (member_def)* "}"

?read: (NAME ".")+ NAME -> read
?write: (NAME ".")+ NAME "=" expr


?assignment: write
            | "let" variable "=" expr -> let_definition
            | "let" "mut" variable "=" expr -> let_mut_definition
            | variable "=" expr -> regular_assign

index: expr "[" expr "]"
?value: function
    | call
    | read
    | index
    | variable
    | literal

literal: NUMBER
    | FLOAT_NUMBER
    | STRING
    | vector
    | "@" -> obj
    | "true" -> true
    | "false" -> false

vector: "[" (expr ",")* (expr)* "]"

args: "|" (variable ",")* (variable)* "|"
retval: "return" (expr ",")* expr ";"
function: args "{" (instruction)* "}" -> function_def_no_return
        | args "{" (instruction)* retval "}" -> function_def_return

while: "while" expr "{" (instruction)* "}" -> while_loop
conditional: "?" expr expr ":" expr

parameters: (expr ",")* (expr)*
call: (NAME ".")+ NAME "(" parameters ")" -> method
    | variable "(" parameters ")"
    | expr "(" parameters ")"


?variable: NAME
        | NAME "&" -> foreign_variable


NUMBER: /0|[1-9]\d*/i
FLOAT_NUMBER: /((\d+\.\d*|\.\d+)(e[-+]?\d+)?|\d+(e[-+]?\d+))/i
STRING : /[ubf]?r?("(?!"").*?(?<!\\)(\\\\)*?"|'(?!'').*?(?<!\\)(\\\\)*?')/i
NAME: /[a-zA-Z_]\w*/
COMMENT: /\/\/[^\n]*/
//COMMENT: /#[^\n]*/

%ignore /[\t \f\n]+/  // WS
%ignore /\\[\t \f\n]*\r?\n/   // LINE_CONT
%ignore COMMENT
'''

BASEDIR = dirname(argv[0])

OUTPUT_DIR = relpath("target/")
RESOURCES_DIR = BASEDIR + "/include/"

STD_DIR = RESOURCES_DIR + "std/"
CABLE_DIR = RESOURCES_DIR + "cable/"