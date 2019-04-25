#pragma once
#include "../cable/cable.cpp"

const Fn io_smart_print = Fn([] (Value things_to_print) {
    for (int i=0; i < things_to_print.len().get_i32().unwrap(); i++) {
        cout << things_to_print[i].call_method("__str__", Value())[0].to_string();
    }
    cout << endl;
    return Value();
});