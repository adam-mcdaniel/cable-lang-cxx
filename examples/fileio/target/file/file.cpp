#include "../cable/cable.cpp"
#include <fstream>
#include <string>

const Fn read_file_fn = Fn([](Value arguments) {
    string file_name = arguments[0].get_string().unwrap();

    ifstream ifs(file_name);
    string content((istreambuf_iterator<char>(ifs)),
                        (istreambuf_iterator<char>()));

    return Value(content);
});


const Fn write_file_fn = Fn([](Value inputs) {
    string file_name = inputs[0].get_string().unwrap();
    string content = inputs[1].get_string().unwrap();

    ofstream ofs(file_name);
    ofs << content;

    return Value();
});