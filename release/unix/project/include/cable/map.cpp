#pragma once
#include <map>
#include "option.cpp"
using namespace std;


template<typename K, typename V>
class Map {
    map<K, V> m;

public:
    Map() {}

    bool operator ==(Map<K, V> m) {
        return this->m == m.m;
    }

    bool operator !=(Map<K, V> m) {
        return this->m != m.m;
    }

    void set(K k, V v) {
        this->m.insert(pair<K, V>(k, v));
    }

    Option<V> get(K k) {
        Option<V> result;

        if(this->m.find(k) != this->m.end()) {
            result = Option<V>::Some(this->m[k]);
        } else {
            result = Option<V>::None();
        }

        return result;
    }
};