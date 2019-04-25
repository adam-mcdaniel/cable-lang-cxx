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

Value prints = Value(io_smart_print);
Value Just = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value d = CABLELANG__PARAMS[Value(0)]; Value self = Value();	*self.get_member("data") = d;	*self.get_member("__bool__") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; return Value(L({self, Value(1)}));}));	*self.get_member("__str__") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; return Value(L({self, *self.get_member("data")}));}));	*self.get_member("unwrap") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; return Value(L({self, *self.get_member("data")}));}));	return self;}));
Value Nothing = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = Value();	*self.get_member("__bool__") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; return Value(L({self, Value(0)}));}));	*self.get_member("__str__") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; return Value(L({self, Value("Nothing")}));}));	*self.get_member("unwrap") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; return Value(L({self, Value()}));}));	return self;}));
Value If = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value a = CABLELANG__PARAMS[Value(0)]; Value b = CABLELANG__PARAMS[Value(1)]; Value c = CABLELANG__PARAMS[Value(2)]; while ((a.call_method("__bool__", Value(L({})))[Value(0)]).to_bool()) {return b(Value(L({})));;};	return c(Value(L({})));}));
Value n = Just(Value(L({Value(5)})));
If(Value(L({n, Value(Fn([&] (Value CABLELANG__PARAMS) {
println(Value(L({Value("N is something")})));	
print(Value(L({Value("N is ")})));	
prints(Value(L({n})));return Value();
})), Value(Fn([&] (Value CABLELANG__PARAMS) {
println(Value(L({Value("N is nothing")})));return Value();
}))})));

return 0;
}