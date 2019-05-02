#include "io/io.cpp"
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
;
Value prints = Value(io_smart_print);
Value String = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value s = __CABLELANG__PARAMS__[Value(0)]; Value self = Value();	*self.get_member("data") = s;	*self.get_member("__str__") = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value self = __CABLELANG__PARAMS__[Value(0)]; return Value(L({self, *self.get_member("data")}));}));	return self;}));
prints(Value(L({String(Value(L({Value("5")})))})));

return 0;
}