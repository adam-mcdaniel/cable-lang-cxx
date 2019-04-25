#include "cable/cable.cpp"

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
Value n = Value(0);
Value a = Value(0.0);
Value b = Value(1.0);
Value c = Value(0.0);
while ((n < Value(1000)).to_bool()) {c = a+b;
a = b;
b = c;
println(Value(L({a})));
n = n+Value(1);};

return 0;
}