#include <any>
#include <string>
#include <iostream>
#include <functional>
#include <cstdlib>
#include "option.cpp"
#include "list.cpp"
#include "map.cpp"
#include "value.cpp"
using namespace std;

typedef Function<Value, Value> Fn;


List<Value> L(vector<Value> v) {
    return List<Value>(v);
}


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

const Fn append_fn = Fn([](Value list_and_obj) {
    Value list = list_and_obj[Value(0)];
    Value obj = list_and_obj[Value(1)];
    list.push(obj);
    return list;
});

const Fn pop_fn = Fn([](Value list) {
    Value l = list[Value(0)];
    Value result = l.pop();
    return Value(L({l, result}));
});


int main() {
    auto print = Value(print_fn);
    auto println = Value(println_fn);
    auto append = Value(append_fn);
    auto pop = Value(pop_fn);
Value List = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = Value();	*self.get_member("list") = Value(Value(L({})));	*self.get_member("len") = Value(0);	*self.get_member("push") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; Value a = CABLELANG__PARAMS[Value(1)]; *self.get_member("list") = append(Value(L({*self.get_member("list"), a})));	*self.get_member("len") = *self.get_member("len")+Value(1);	return self;}));	*self.get_member("pop") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; Value list_and_result = pop(Value(L({*self.get_member("list")})));	*self.get_member("list") = list_and_result[Value(0)];	Value result = list_and_result[Value(1)];	*self.get_member("len") = *self.get_member("len")-Value(1);	return Value(L({self, result}));}));	*self.get_member("print") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; println(Value(L({*self.get_member("list")})));	return self;}));	return self;}));
Value l = List(Value(L({})));
l.call_method("print", Value(L({})));
l.call_method("push", Value(L({Value("a")})));
l.call_method("push", Value(L({Value("b")})));
l.call_method("push", Value(L({Value("c")})));
l.call_method("push", Value(L({Value("d")})));
l.call_method("push", Value(L({Value("e")})));
l.call_method("print", Value(L({})));
l.call_method("pop", Value(L({})));
l.call_method("print", Value(L({})));
Value Test = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value l = CABLELANG__PARAMS[Value(0)]; Value self = Value();	*self.get_member("list") = l;	self.get_member("list")->call_method("push", Value(L({Value(5)})));	*self.get_member("init") = Value(Fn([&] (Value CABLELANG__PARAMS) {
Value self = CABLELANG__PARAMS[Value(0)]; self.get_member("list")->call_method("print", Value(L({})));	return self;}));	return self;}));
Value t = Test(Value(L({l})));
t.call_method("init", Value(L({})));return 0;
}