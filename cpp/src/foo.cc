#include "foo.h"

#include <iostream>

int foo(Foo* foo) { return bar(&foo->value, foo->msg); }

int bar(int* value, char* msg) {
  std::cout << "bar() called in C++" << std::endl;
  std::cout << "-> value in C++: " << *value << std::endl;
  std::cout << "-> msg in C++: " << msg << std::endl;

  if (*value == 0) {
    std::cout << "-> returning 0" << std::endl;
    return 0;
  } else {
    std::cout << "-> returning 1" << std::endl;
    return 1;
  }
}

int register_bar_callback(CALLBACK cb) {
  std::cout << "register_bar_callback() called in C++" << std::endl;

  int value = 42;
  char* msg = "Hello World!";
  std::cout << "-> value in C++: " << value << std::endl;
  std::cout << "-> msg in C++: " << msg << std::endl;

  std::cout << "-> calling registered function in C++" << std::endl;
  cb(&value, msg);

  return 0;
}