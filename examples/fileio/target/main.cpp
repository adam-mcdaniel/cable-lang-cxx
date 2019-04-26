#include "file/file.cpp"
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
Value read_file = Value(read_file_fn);
Value write_file = Value(write_file_fn);
Value File = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value name = __CABLELANG__PARAMS__[Value(0)]; Value self = Value();	*self.get_member("name") = name;	*self.get_member("read") = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value self = __CABLELANG__PARAMS__[Value(0)]; return Value(L({self, read_file(Value(L({*self.get_member("name")})))}));}));	*self.get_member("write") = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value self = __CABLELANG__PARAMS__[Value(0)]; Value content = __CABLELANG__PARAMS__[Value(1)]; return Value(L({self, write_file(Value(L({*self.get_member("name"), content})))}));}));	*self.get_member("append") = Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value self = __CABLELANG__PARAMS__[Value(0)]; Value content = __CABLELANG__PARAMS__[Value(1)]; return Value(L({self, write_file(Value(L({*self.get_member("name"), read_file(Value(L({*self.get_member("name")})))+content})))}));}));	return self;}));;
println(Value(L({File(Value(L({Value("test.txt")}))).call_method("read", Value(L({})))})));
Value f = File(Value(L({Value("whoa.txt")})));
Value n = Value(0);
while ((n < Value(100)).to_bool()) {f.call_method("append", Value(L({Value("whoa")})));
n = n+Value(1);};
println(Value(L({f.call_method("read", Value(L({})))})));
f.call_method("write", Value(L({Value("test")})));
println(Value(L({f.call_method("read", Value(L({})))})));

return 0;
}