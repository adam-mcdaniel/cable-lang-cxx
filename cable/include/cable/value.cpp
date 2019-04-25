#pragma once
#include <any>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include "function.cpp"
#include "option.cpp"
#include "list.cpp"
#include "map.cpp"
using namespace std;


typedef int i32;
typedef double f64;

enum Type {
    NoneType,
    ListType,
    String,
    FunctionType,
    I32,
    F64
};

// Works with everything but list.
template<typename T>
string num_to_string(T t) {
    ostringstream s;
    s << t;
    return s.str();
}


class Value {
public:
    any value;
    Map<string, Value*> members;
    Type type;

    void push(Value v) {
        auto list_option = this->get_list();
        if (list_option) {
            auto list = list_option.unwrap();
            list.push(v);
            this->set_value(list);
        }
    }

    Value pop() {
        auto list_option = this->get_list();
        if (list_option) {
            auto list = list_option.unwrap();
            auto result = list.pop();
            this->set_value(list);
            return result.unwrap();
        }
        return Value();
    }

    void remove(Value i) {
        auto list_option = this->get_list();
        if (list_option) {
            auto list = list_option.unwrap();
            if (i.get_i32()) {
                list.remove(i.get_i32().unwrap());
                this->set_value(list);
            }
        }
    }

    Value len() {
        auto list_option = this->get_list();
        if (list_option) {
            return list_option.unwrap().len();
        }
        return Value(0);
    }
    
    template<typename T>
    void set_value(T t) {
        *this = Value(t);
    }

    Value() {
        this->type = Type::NoneType;
    }

    Value(i32 value) {
        this->value = value;
        this->type = Type::I32;
    }

    Value(f64 value) {
        this->value = value;
        this->type = Type::F64;
    }

    Value(string value) {
        this->value = value;
        this->type = Type::String;
    }

    Value(vector<Value> value) {
        this->value = List(value);
        this->type = Type::ListType;
    }

    Value(List<Value> value) {
        this->value = value;
        this->type = Type::ListType;
    }

    Value(Function<Value, Value> f) {
        this->value = f;
        this->type = Type::FunctionType;
    }

    Value* get_member(string name) {
        auto result = this->members.get(name);
        if (!result) {
            this->members.set(name, new Value());
            result = this->members.get(name);
        }
        return result.unwrap();
    }

    Value call_method(string name, Value v) {
        Value f = *this->get_member(name);
        Value val = f(Value(vector<Value>{*this}) + v);
        Option<List<Value>> result = val.get_list();
        if (result) {
            Option<Value> self = result.unwrap().at(0);
            if (self) {
                *this = self.unwrap();
            }
            Value ret_val = result.unwrap();
            ret_val.remove(0);
            return ret_val;
        } else {
            *this = val;
        }

        return Value();
    }

    string to_string() {
        return this->format().get_string().unwrap();
    }

    Value call(Value v) {
        Value result;
        auto f = this->get_function();
        if (f) {
            result = f.unwrap().call(v);
        }
        return result;
    }

    bool to_bool() {
        return this->get_i32().unwrap() != 0;
    }

    Value operator ||(Value v) {
        return Value(v.to_bool() || this->to_bool());
    }

    Value operator &&(Value v) {
        return Value(v.to_bool() && this->to_bool());
    }

    Value operator !() {
        return Value(! i32(this->to_bool()));
    }

    Value operator !=(Value v) {
        return Value(this->type != v.type || this->to_string() != v.to_string() || this->members != v.members);
    }

    Value operator ==(Value v) {
        return Value(this->type == v.type && this->to_string() == v.to_string() && this->members == v.members);
    }

    Value operator <(Value v) {
        Value result;
        switch(this->type) {
        case Type::I32:
            result = Value(this->get_i32().unwrap() < v.get_i32().unwrap());
            break;

        case Type::F64:
            result = Value(this->get_f64().unwrap() < v.get_f64().unwrap());
            break;
            
        case Type::String:
            result = Value(this->get_string().unwrap() < v.get_string().unwrap());
            break;
            
        default:
            result = Value();
        }
        return result;
    }

    Value operator >(Value v) {
        Value result;
        switch(this->type) {
        case Type::I32:
            result = Value(this->get_i32().unwrap() > v.get_i32().unwrap());
            break;

        case Type::F64:
            result = Value(this->get_f64().unwrap() > v.get_f64().unwrap());
            break;
            
        case Type::String:
            result = Value(this->get_string().unwrap() > v.get_string().unwrap());
            break;
            
        default:
            result = Value();
        }
        return result;
    }

    Value operator >=(Value v) {
        return (*this > v) || (*this == v);
    }

    Value operator <=(Value v) {
        return (*this < v) || (*this == v);
    }

    Value operator ()(Value v) {
        return this->call(v);
    }

    Value operator [](Value v) {
        Option<Value> result = this->get_list().unwrap().at(v.get_i32().unwrap());
        return result.unwrap();
    }

    Value operator +(Value v) {
        Value result;
        switch (this->type) {
            case Type::ListType:
                result = Value(this->get_list().unwrap() + v.get_list().unwrap()); break;

            case Type::String:
                result = Value(this->get_string().unwrap() + v.get_string().unwrap()); break;

            case Type::I32:
                result = Value(this->get_i32().unwrap() + v.get_i32().unwrap()); break;

            case Type::F64:
                result = Value(this->get_f64().unwrap() + v.get_f64().unwrap()); break;

            default:
                result = Value();
        }
        return result;
    }

    Value operator -() {
        Value result;
        switch (this->type) {
            case Type::I32:
                result = Value(-this->get_i32().unwrap()); break;

            case Type::F64:
                result = Value(-this->get_f64().unwrap()); break;

            default:
                result = Value();
        }
        return result;
    }

    Value operator -(Value v) {
        return *this + (-v);
    }

    Value operator *(Value v) {
        Value result;

        switch (this->type) {
            case Type::I32:
                result = Value(this->get_i32().unwrap() * v.get_i32().unwrap()); break;

            case Type::F64:
                result = Value(this->get_f64().unwrap() * v.get_f64().unwrap()); break;
                
            default:
                result = Value();
        }
        return result;
    }

    Value operator /(Value v) {
        Value result;
        switch (this->type) {
            case Type::I32:
                result = Value(this->get_i32().unwrap() / v.get_i32().unwrap()); break;

            case Type::F64:
                result = Value(this->get_f64().unwrap() / v.get_f64().unwrap()); break;

            default:
                result = Value();
        }
        return result;
    }

    Value format() {
        string result = "";
        switch (this->type) {
            case Type::ListType:
                return Value(this->get_list().unwrap().to_string());
                break;
            case Type::String:
                if (this->get_string()) {
                    return Value(this->get_string().unwrap());
                } else {
                    return Value("");
                }
                break;
            case Type::I32:
                if (this->get_i32()) {
                    return Value(num_to_string<i32>(this->get_i32().unwrap()));
                } else {
                    return Value("");
                }
                break;
            case Type::F64:
                if (this->get_f64()) {
                    return Value(num_to_string<f64>(this->get_f64().unwrap()));
                } else {
                    return Value("");
                }
                break;
            case Type::FunctionType:
                return Value("<Function>");
                break;
            case Type::NoneType:
                return Value("None");
                break;
        }
    }

    Option<Function<Value, Value>> get_function() {
        Option<Function<Value, Value>> result;
        try {
            result = Option<Function<Value, Value>>::Some(
                any_cast<Function<Value, Value>>(this->value)
            );
        }
        catch (const bad_any_cast& e) {
            result = Option<Function<Value, Value>>::None();
        }
        return result;
    }


    Option<string> get_string() {
        Option<string> result;
        try {
            result = Option<string>::Some(
                any_cast<string>(this->value)
            );
        }
        catch (const bad_any_cast& e) {
            result = Option<string>::None();
        }
        return result;
    }


    Option<List<Value>> get_list() {
        Option<List<Value>> result;
        try {
            result = Option<List<Value>>::Some(
                any_cast<List<Value>>(this->value)
            );
        }
        catch (const bad_any_cast& e) {
            result = Option<List<Value>>::None();
        }
        return result;
    }

    Option<i32> get_i32() {
        Option<i32> result;
        try {
            result = Option<i32>::Some(
                any_cast<i32>(this->value)
            );
        }
        catch (const bad_any_cast& e) {
            result = Option<i32>::None();
        }
        return result;
    }

    Option<f64> get_f64() {
        Option<f64> result;
        try {
            result = Option<f64>::Some(
                any_cast<f64>(this->value)
            );
        }
        catch (const bad_any_cast& e) {
            result = Option<f64>::None();
        }
        return result;
    }
};


ostream & operator<<(ostream & os, Value v) {
    os << v.to_string();
    return os;
}