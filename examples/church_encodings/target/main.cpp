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
Value True = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value b = __CABLELANG__PARAMS__[Value(0)]; return a;}));}));
Value False = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value b = __CABLELANG__PARAMS__[Value(0)]; return b;}));}));
Value If = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value b = __CABLELANG__PARAMS__[Value(0)]; return Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value c = __CABLELANG__PARAMS__[Value(0)]; return a(Value(L({b})))(Value(L({c})));}));}));}));
If(Value(L({False})))(Value(L({Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value n = __CABLELANG__PARAMS__[Value(0)]; println(Value(L({Value("true! also "), n})));return Value();
}))})))(Value(L({Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value n = __CABLELANG__PARAMS__[Value(0)]; println(Value(L({Value("false! also "), n})));return Value();
}))})))(Value(L({Value(5)})));

return 0;
}