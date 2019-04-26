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
Value range = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value l = __CABLELANG__PARAMS__[Value(0)]; Value u = __CABLELANG__PARAMS__[Value(1)]; Value result = Value(Value(L({})));	Value n = l;	while ((n < u).to_bool()) {n+=Value(1);
result+=Value(Value(L({n})));};	return result;}));
for (Value x : range(Value(L({Value(0), Value(1000)}))).get_list().unwrap().as_vector()) {println(Value(L({x})));};

return 0;
}