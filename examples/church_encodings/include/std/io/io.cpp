#include "../../cable/cable.cpp"
#include "../str/str.cpp"
#include "../exported/exported.cpp"



const Fn put_fn = Fn([](Value printed_objects) {
    for (int i=0; i < printed_objects.len().get_i32().unwrap(); i++) {
        cout << str.call(Value(L({printed_objects[i]})));
    }
    return Value();
});

const Fn putln_fn = Fn([](Value printed_objects) {
    for (int i=0; i < printed_objects.len().get_i32().unwrap(); i++) {
        // cout << printed_objects[i].call_method("__str__", Value());
        cout << str.call(Value(L({printed_objects[i]})));
    }
    cout << endl;
    return Value();
});