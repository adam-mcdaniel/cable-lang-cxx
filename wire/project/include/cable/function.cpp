#pragma once
#include "map.cpp"
#include "list.cpp"
#include "option.cpp"
#include <functional>


template<typename I, typename O>
class Function {
public:
    Function() {
        this->f = [](I i) { return O(); };
    }

    Function(function<O(I)> f) {
        this->f = f;
    }

    O call(I i) {
        return this->f(i);
    }
    
private:
    function<O(I)> f;
};