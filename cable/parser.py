from lark import Lark, Transformer
from constants import GRAMMAR

def rreplace(s, old, new):
    li = s.rsplit(old, 1) #Split only once
    return new.join(li)


includes = []


# def_prefix = "auto"
def_prefix = "Value"

class CableLangCXXTree(Transformer):
    def __init__(self, path):
        self.path = path

    def read(self, names):
        result = "*" + str(names[0]) + ".get_member(\"" + str(names[1]) + "\")"
        remaining = names[2:]

        for name in remaining:
            result += "->get_member(\"" + str(name) + "\")"
        
        return result

    def cxx(self, values):
        return '\n'.join(values)

    def import_(self, values):
        script = CableLangCXXTree(self.path).transform(
                    Lark(
                        GRAMMAR,
                        start='block',
                        parser='lalr',
                        lexer='standard'
                    ).parse(open(self.path + "/" + values[0].replace("\"", "") + ".cb").read())
                )

        return script

    def include(self, values):
        includes.append('#include {}\n'.format(values[0]))
        return ""

    def foreign_variable(self, values):
        name = values[0]
        return "Value(" + name + ")"

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

    def greater(self, operands):
        return operands[0] + " > " + operands[1]
    def less(self, operands):
        return operands[0] + " < " + operands[1]
    def greatereq(self, operands):
        return operands[0] + " >= " + operands[1]
    def lesseq(self, operands):
        return operands[0] + " <= " + operands[1]

    def or_(self, operands):
        return operands[0] + "||" + operands[1]

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

    def addeq(self, operands):
        return operands[0] + "+=" + operands[1]

    def subtracteq(self, operands):
        return operands[0] + "-=" + operands[1]

    def multiplyeq(self, operands):
        return operands[0] + "*=" + operands[1]

    def divideeq(self, operands):
        return operands[0] + "/=" + operands[1]

    def modeq(self, operands):
        return operands[0] + "%=" + operands[1]

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

    def for_loop(self, values):
        name = values[0]
        vector = values[1]
        body = values[2:]
        return "for (Value " + name + " : " + vector + ".get_list().unwrap().as_vector()) {" + '\n'.join(body) + "}" 

    def literal(self, values):
        return "Value({})".format(values[0])

    def let_mut_definition(self, values):
        return def_prefix + " " + str(values[0]) + " = " + str(values[1])

    def let_definition(self, values):
        return def_prefix + " " + str(values[0]) + " = " + str(values[1])

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
        PARAMS_NAME = "__CABLELANG__PARAMS__"
        # This causes problems with closures.
        # Do not pass by reference.
        # result = "[&] (Value " + PARAMS_NAME + ") {\n"
        
        # This passes by value. Slower but allows more flexible programming
        result = "[=] (Value " + PARAMS_NAME + ") mutable {\n"

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
