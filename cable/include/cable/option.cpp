#pragma once


enum Maybe {
    Just,
    None
};


template<typename T>
class Option {
public:
    Option<T>() {
        this->m = Maybe::None;
    }

    static Option Some(T t) {
        return Option(Maybe::Just, t);
    }

    static Option None() {
        return Option(Maybe::None);
    }

    T unwrap() {
        return this->t;
    }

    operator bool() {
        return this->m == Maybe::Just;
    }

private:
    Maybe m;
    T t;

    Option(Maybe m) {
        this->m = m;
    }

    Option(Maybe m, T t) {
        this->m = m;
        this->t = t;
    }
};
