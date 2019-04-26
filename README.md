# cable-lang-cxx

Cable-lang is a programming language that compiles to C++. It runs very fast, but it's extremely high level. It's also dynamically typed. Here's an example script in Cable-lang.


## Examples

### Basic iterative programming 

```rust
// fibonacci sequence
let n = 0;

let a = 0.0;
let b = 1.0;
let c = 0.0;

while n < 1000 {
    c = a + b;
    a = b;
    b = c;

    println(a);
    n = n + 1;
}
```

### Functional programming 

```rust
// church encodings

let True = |a| {
    return |b| { // closure
        return a;
    }; 
};

let False = |a| {
    return |b| { // closure
        return b;
    }; 
};

let If = |a| {
    return |b| {
        return |c| {
            return a(b)(c);
        }; 
    }; 
};


If(False)(
        |n| {
            println("true! also ", n);
        }
    )
    (
        |n| {
            println("false! also ", n);
        }
    )(5);
```

### Object Oriented programming 

```rust
// include file manipulation foreign functions
include "file/file.cpp"

// bind those functions to a function name
let read_file = read_file_fn&;
let write_file = write_file_fn&;



// Define a constructor
// This is really just a constructor instead of a class,
// It returns an objects with the defined attributes,
// its not really of type File.
let File = |name| {
    // Must define the object to return by yourself!
    let self = @;

    self.name = name;

    self.read = |self| {
        // Return the value of self, or the object will become None
        return self, read_file(self.name);
    };

    self.write = |self, content| {
        // Return the value of self, or the object will become None
        return self, write_file(self.name, content);
    };

    self.append = |self, content| {
        // Return the value of self, or the object will become None
        return self, write_file(self.name, read_file(self.name) + content);
    };

    return self;
};

// Print contents of `test.txt`
println(
    File("test.txt").read()
);

// Open file `whoa.txt`
let f = File("whoa.txt");

// Append `whoa` 100 times to end of `whoa.txt`
let n = 0;
while n < 100 {
    f.append("whoa");
    n = n + 1;
}


// Print the contents of `whoa.txt`
println(
    f.read()
);

// Overwrite the contents of `whoa.txt` with "test"
f.write("test");


// Print the contents of `whoa.txt`
println(
    f.read()
);
```