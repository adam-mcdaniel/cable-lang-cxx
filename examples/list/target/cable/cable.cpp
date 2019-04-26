#pragma once
#include <iostream>
#include <vector>
#include "option.cpp"
#include "list.cpp"
#include "map.cpp"
#include "value.cpp"
#include "function.cpp"
using namespace std;

typedef Function<Value, Value> Fn;

List<Value> L(vector<Value> v) {
    return List<Value>(v);
}