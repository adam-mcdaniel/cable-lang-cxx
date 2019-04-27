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

const Fn len_fn = Fn([](Value l) {
    return l.len();
});

const Fn range_fn = Fn([](Value lower_and_upper) {
    Value l = lower_and_upper[Value(0)];
    Value u = lower_and_upper[Value(1)];

    Value result = Value(L({}));
    for (int i=l.get_i32().unwrap(); i < u.get_i32().unwrap(); i++) {
        result.push(Value(i));
    }

    return result;
});

const Fn map_fn = Fn([](Value list_and_function) {
    Value l = list_and_function[Value(0)];
    Value f = list_and_function[Value(1)];

    Value result = Value(L({}));
    for (int i=0; i < l.len().get_i32().unwrap(); i++) {
        result.push(f(Value(L({l[i]}))));
    }

    return result;
});