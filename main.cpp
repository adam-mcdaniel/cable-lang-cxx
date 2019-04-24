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



int main() {
    auto print = Value(print_fn);
    auto println = Value(println_fn);





println(Value(L({Value("test")})));
print(Value(L({(Value(1)+Value(3))*Value(5)})));

    // auto f = Value(Fn([](Value v) {
    //     v.call_method("m", Value(100));
    //     return v;
    // }));

    // auto a = Value();
    // *a.get_member("b")->get_member("m") = Value(method);

    // *a.get_member("b") = f(*a.get_member("b"));

    // cout << *a.get_member("b")->get_member("c") << endl;

    // a.get_member("b")->call_method("m", Value(5));


    // auto x = Value(L({}));

    // cout << x << endl;
    // cout << x.pop() << endl;
    // cout << x << endl;
    // x.push(Value("string") + Value("test"));
    // cout << x << endl;
    // x.push(Value(Fn([](Value v) {cout << "in fn" << endl; return v; })));
    // cout << x << endl;

    // auto l1 = List<Int>({Int(1), Int(2), Int(3)});
    // auto l2 = List<Int>({Int(4), Int(5), Int(6)});

    // cout << (l1 + l2).to_string() << endl;
    // cout << *a.get_member("b")->get_member("c") << endl;

    return 0;
}