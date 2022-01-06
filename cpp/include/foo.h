#pragma once
#include <string>

struct Foo {
  int value;
  char* msg;
};

char g_buf[32] = "012345678";
typedef int (*CALLBACK)(int*, char*);
CALLBACK g_callback;

extern "C" {
int foo(Foo* foo);
int bar(int* value, char* msg);
int register_bar_callback(CALLBACK cb);
}
