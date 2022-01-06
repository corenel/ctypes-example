#include "foo.h"

#include <cstring>
#include <iostream>
#include <memory>

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

  // std::string msg_str = "Hello World!";
  // char msg[msg_str.length() + 1];
  // std::strcpy(msg, msg_str.c_str());
  // char* msg = "Hello World!";

  g_callback = cb;
  int len_buf = std::strlen(g_buf) + 1;

  std::cout << "-> len_buf in C++ before callback: " << len_buf << std::endl;
  std::cout << "-> buf in C++ before callback: " << g_buf << std::endl;

  std::cout << "-> calling registered function in C++" << std::endl;
  g_callback(&len_buf, g_buf);

  std::cout << "-> lem_buf in C++ aftering callback: " << len_buf << std::endl;
  std::cout << "-> buf in C++ aftering callback: " << g_buf << std::endl;

  return 0;
}
