#include "../../cable/cable.cpp"


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

const Fn remove_fn = Fn([](Value list_and_index) {
    Value l = list_and_index[Value(0)];
    l.remove(list_and_index[Value(1)]);
    return l;
});