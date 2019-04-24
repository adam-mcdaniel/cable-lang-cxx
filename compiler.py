# from lark import Lark
import sys
from lark import Lark, Transformer

grammar = r'''
    start: (instruction)+

    instruction: while
               | expr ";"

    ?block: (instruction)+

    ?expr: assignment
        | class_def
        | conditional
        | value
        | "(" expr ")" -> wrapped_expr
        | math

    eq: expr "==" expr
      | expr "is" expr
    noteq: expr "!=" expr
    not_: "!" expr
       | "not" expr
    and_: expr "&&" expr
       | expr "and" expr
    add: expr "+" expr
    subtract: expr "-" expr
    multiply: expr "*" expr
    divide: expr "/" expr
    mod: expr "%" expr

    ?math: add
        | subtract
        | multiply
        | divide
        | mod
        | eq
        | noteq
        | not_
        | and_

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
    STRING : /[ubf]?r?("(?!"").*?(?<!\\)(\\\\)*?"|'(?!'').*?(?<!\\)(\\\\)*?')/i
    NAME: /[a-zA-Z_]\w*/
    //COMMENT: /#[^\n]*/
    COMMENT: /\/\/[^\n]*/

    %ignore /[\t \f\n]+/  // WS
    %ignore /\\[\t \f\n]*\r?\n/   // LINE_CONT
    %ignore COMMENT
'''


def rreplace(s, old, new):
    li = s.rsplit(old, 1) #Split only once
    return new.join(li)

class CableLangCXXTree(Transformer):
    def read(self, names):
        result = "*" + str(names[0]) + ".get_member(\"" + str(names[1]) + "\")"
        remaining = names[2:]

        for name in remaining:
            result += "->get_member(\"" + str(name) + "\")"
        
        return result

    def index(self, values):
        name = values[0]
        index = values[1]
        return name + "[" + index + "]"

    def vector(self, objects):
        return "Value(L({" + ', '.join(objects) + "}))"

    def true(self, _):
        return "Value(1)"

    def false(self, _):
        return "Value(0)"

    def block(self, exprs):
        return '\n'.join(exprs)

    def wrapped_expr(self, exprs):
        return '(' + exprs[0] + ')'

    def parameters(self, parameters):
        return "Value(L({" + ', '.join(parameters) + "}))"

    def not_(self, operands):
        return "! " + operands[0]

    def and_(self, operands):
        return operands[0] + "&&" + operands[1]

    def eq(self, operands):
        return operands[0] + "==" + operands[1]

    def noteq(self, operands):
        return operands[0] + "!=" + operands[1]

    def add(self, operands):
        return operands[0] + "+" + operands[1]

    def subtract(self, operands):
        return operands[0] + "-" + operands[1]

    def multiply(self, operands):
        return operands[0] + "*" + operands[1]

    def divide(self, operands):
        return operands[0] + "/" + operands[1]

    def mod(self, operands):
        return operands[0] + "%" + operands[1]

    def obj(self, _):
        return "Value()"

    def call(self, names):
        result = str(names[0]) + "(" + str(names[1]) + ")"
        return result

    def method(self, values):
        names = values[:-1]
        parameters = values[-1]

        result = names[0]
        remaining = names
        if len(names) > 2:

            result = str(names[0]) + ".get_member(\"" + str(names[1]) + "\")"
            remaining = names[2:]

            for name in remaining[:-1]:
                result += "->get_member(\"" + str(name) + "\")"
            
            result += "->call_method(\"" + str(remaining[-1]) + "\", "
            result += parameters + ")"
        else:
            result += ".call_method(\"" + str(remaining[-1]) + "\", "
            result += parameters + ")"

        return result

    def while_loop(self, values):
        condition = values[0]
        body = values[1:]

        return "while ((" + str(condition) + ").to_bool()) {" + '\n'.join(body) + "}" 

    def literal(self, values):
        return "Value({})".format(values[0])

    def let_mut_definition(self, values):
        return "Value " + str(values[0]) + " = " + str(values[1])

    def let_definition(self, values):
        return "Value " + str(values[0]) + " = " + str(values[1])

    def instruction(self, value):
        return str(value[0]) + ";"

    def retval(self, values):
        if len(values) == 1:
            return "return " + str(values[0]) + ";"
        elif len(values) > 1:
            return "return Value(L({" + ', '.join(values) + "}));"
        else:
            return "return Value();"


    def write(self, values):
        names = values[:-1]
        new_value = values[-1]


        result = "*" + str(names[0]) + ".get_member(\"" + str(names[1]) + "\")"
        remaining = names[2:]

        for name in remaining:
            result += "->get_member(\"" + str(name) + "\")"
        
        result += " = " + new_value
        return result

    def regular_assign(self, values):
        variable_name = values[0]
        value = values[1]
        return variable_name + " = " + value

    def args(self, parameters):
        PARAMS_NAME = "CABLELANG__PARAMS"
        result = "[&] (Value " + PARAMS_NAME + ") {\n"

        for i, p in enumerate(parameters):
            result += "Value " + str(p) + " = " + PARAMS_NAME + "[Value(" + str(i) + ")]; "

        return result

    def function_def_no_return(self, values):
        args = values[0]
        body = values[1:]

        return 'Value(Fn(' + args + '\t\n'.join(body) + 'return Value();\n' + '}))'

    def function_def_return(self, values):
        args = values[0]
        body = values[1:]

        return 'Value(Fn(' + args + '\t'.join(body) + '}))'


l = Lark(grammar, start='block', parser='lalr', lexer='standard')
# l = Lark(grammar)
# s x: > println!
# s s method: > ! s=

# parse = lambda text: CableLangTree().transform(l.parse(text))
# parse = lambda text: l.parse(text).pretty()
# parse = lambda text: '\n'.join(CableLangCXXTree().transform(l.parse(text)).pretty()[5:].splitlines())
# parse = lambda text: CableLangCXXTree().transform(l.parse(text))
def parse(text):
    try:
        return CableLangCXXTree().transform(l.parse(text))
    except Exception as e:
        # print(dir(e))
        # print(e.token)
        if e.token == '':
            print("==[ ERROR ]===> Unexpected end of file")

        else: print("==[ ERROR ]===> Unexpected token: '{}'".format(e.token))
        return ""

if len(sys.argv) >= 2:
    with open("test.cpp", "w") as f:
        f.write("""#include <any>
#include <string>
#include <iostream>
#include <functional>
#include <cstdlib>
#include "option.cpp"
#include "list.cpp"
#include "map.cpp"
#include "value.cpp"
using namespace std;

typedef Function<Value, Value> Fn;


List<Value> L(vector<Value> v) {
    return List<Value>(v);
}


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

const Fn append_fn = Fn([](Value list_and_obj) {
    Value list = list_and_obj[Value(0)];
    Value obj = list_and_obj[Value(1)];
    list.push(obj);
    return list;
});

const Fn pop_fn = Fn([](Value list) {
    Value l = list[Value(0)];
    Value result = l.pop();
    return Value(L({l, result}));
});


int main() {
    auto print = Value(print_fn);
    auto println = Value(println_fn);
    auto append = Value(append_fn);
    auto pop = Value(pop_fn);
""")

        f.write(
            parse(open(sys.argv[1]).read())
        )

        f.write("return 0;\n}")