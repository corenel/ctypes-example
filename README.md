# ctypes-example

A simple example for calling C++ functions in Python by `ctypes`.

## Features

- call C++ function `int bar(int* value, char* msg)` with argumenets:
- call C++ function `int foo(Foo* foo)` with pointer to custom structure `Foo`
- call C++ function `int register_bar_callback(CALLBACK cb)` with a C callable function pointers from Python callables (a.k.a, register a callback function)

## Usage

```bash
cd ctypes-example
# build shared library
mkdir build && cd build
cmake ..
make
# test calling in Python
cd ../python
python test_foo.py
```

## Outputs

Outputs from `register_bar_callback` test:

```bash
$ python test_foo.py
=== Running test_callback() in Python ===
Calling register_bar_callback() in Python
register_bar_callback() called in C++
-> len_buf in C++ before callback: 10
-> buf in C++ before callback: 012345678
-> calling registered function in C++
Callback called in Python
-> len_buf received in Python: 10
-> len_buf modified in Python 13
-> buf modified in Python: Hello, World!
-> lem_buf in C++ aftering callback: 13
-> buf in C++ aftering callback: Hello, World!
Return value in Python: 0
```
