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
