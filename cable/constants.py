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
start: (instruction)+
?block: (instruction)+
//start: (instruction | include)+
//?block: (instruction | include)+

include: "include" STRING
import_: "import" STRING

instruction: include ";"
            | import_ ";"
            | while
            | for
            | if
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
addeq: (read | variable) "+=" expr
subtract: expr "-" expr
subtracteq: (read | variable) "-=" expr
multiply: expr "*" expr
multiplyeq: (read | variable) "*=" expr
divide: expr "/" expr
divideeq: (read | variable) "/=" expr
mod: expr "%" expr
modeq: (read | variable) "%=" expr
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
     | expr "." (NAME ".")* NAME -> read
?write: (NAME ".")+ NAME "=" expr


?assignment: addeq
        | subtracteq
        | multiplyeq
        | divideeq
        | modeq
        | write
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

if: "if" expr "{" (instruction)* "}" -> if_statement
while: "while" expr "{" (instruction)* "}" -> while_loop
for: "for" NAME "in" expr "{" (instruction)* "}" -> for_loop
conditional: "?" expr expr ":" expr

parameters: (expr ",")* (expr)*
call: (NAME ".")+ NAME "(" parameters ")" -> method
    | expr "." (NAME ".")* NAME "(" parameters ")" -> method
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