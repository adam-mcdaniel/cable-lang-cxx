#pragma once
#include <vector>
#include "option.cpp"
using namespace std;


template<typename T>
class List {
private:
    vector<T> t;
    int length;

public:
    List() {
        this->t = {};
        this->length = 0;
    }

    List(vector<T> t) {
        this->t = t;
        this->length = t.size();
    }

    vector<T> as_vector() {
        return this->t;
    }

    void push(T t) {
        this->t.push_back(t);
        this->length++;
    }

    void remove(int i) {
        if (i < this->len()) {
            this->t.erase(this->t.begin()+i);
        }
        this->length--;
    }

    Option<T> at(int i) {
        Option<T> result;

        if (this->len() > i) {
            result = Option<T>::Some(this->t[i]);
        } else {
            result = Option<T>::None();
        }

        return result;
    }

    Option<T> pop() {
        Option<T> result;

        if (length > 0) {
            result = Option<T>::Some(this->t.back());
            this->t.pop_back();
            this->length--;
        } else {
            result = Option<T>::None();
        }

        return result;
    }

    int len() {
        return this->length;
    }

    List<T> operator +(List<T> l) {
        auto vector1 = this->t;
        auto vector2 = l.t;
        vector1.insert(vector1.end(), vector2.begin(), vector2.end());

        return List<T>(vector1);
    }

    string to_string() {
        string result = "[";
        for (int i=0; i<this->len(); i++) {
            result += this->at(i).unwrap().to_string();
            result += ", ";
        }

        if (this->len() > 0) {
            result.pop_back();
            result.pop_back();
        }

        result += "]";
        return result;
    }
};