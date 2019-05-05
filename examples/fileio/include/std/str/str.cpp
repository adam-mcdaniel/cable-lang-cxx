#pragma once
#include "../../cable/cable.cpp"
#include <sstream>

const Fn raw_to_string_fn = Fn([](Value s) {
    return s[0].format();
});

const Fn raw_type_fn = Fn([](Value s) {
    return s[0].get_type_str();
});