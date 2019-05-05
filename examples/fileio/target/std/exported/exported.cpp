#pragma once
#include "../../cable/cable.cpp"
#include "../str/str.cpp"

Value raw_type = raw_type_fn;
Value raw_to_string = raw_to_string_fn;

Value __case_none__ = Value(Fn([] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; Value b = __CABLELANG__PARAMS__[Value(1)]; Value c = __CABLELANG__PARAMS__[Value(2)]; if ((raw_type(Value(L({a})))==Value("NoneType")).to_bool()) {return b;;};	
if ((raw_type(Value(L({a})))!=Value("NoneType")).to_bool()) {return c;;};return Value();
}));
Value value = Value(Fn([] (Value __CABLELANG__PARAMS__) mutable {
Value o = __CABLELANG__PARAMS__[Value(0)]; return __case_none__(Value(L({o, Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return a.call_method("__value__", Value(L({})));}))(Value(L({o}))), o})));}));
Value str = Value(Fn([] (Value __CABLELANG__PARAMS__) mutable {
Value o = __CABLELANG__PARAMS__[Value(0)]; return __case_none__(Value(L({o, Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return a.call_method("__str__", Value(L({})));}))(Value(L({o}))), raw_to_string(Value(L({o})))})));}));
Value boolean = Value(Fn([] (Value __CABLELANG__PARAMS__) mutable {
Value o = __CABLELANG__PARAMS__[Value(0)]; return __case_none__(Value(L({o, Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return a.call_method("__bool__", Value(L({})));}))(Value(L({o}))), o})));}));
Value integer = Value(Fn([] (Value __CABLELANG__PARAMS__) mutable {
Value o = __CABLELANG__PARAMS__[Value(0)]; return __case_none__(Value(L({o, Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return a.call_method("__integer__", Value(L({})));}))(Value(L({o}))), o})));}));
Value decimal = Value(Fn([] (Value __CABLELANG__PARAMS__) mutable {
Value o = __CABLELANG__PARAMS__[Value(0)]; return __case_none__(Value(L({o, Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return a.call_method("__decimal__", Value(L({})));}))(Value(L({o}))), o})));}));
Value function = Value(Fn([] (Value __CABLELANG__PARAMS__) mutable {
Value o = __CABLELANG__PARAMS__[Value(0)]; return __case_none__(Value(L({o, Value(Fn([=] (Value __CABLELANG__PARAMS__) mutable {
Value a = __CABLELANG__PARAMS__[Value(0)]; return a.call_method("__fn__", Value(L({})));}))(Value(L({o}))), o})));}));