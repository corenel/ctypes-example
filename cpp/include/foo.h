#include <string>

struct Foo {
  int value;
  char* msg;
};

typedef int (*CALLBACK)(int*, char*);

extern "C" {
int foo(Foo* foo);
int bar(int* value, char* msg);
int register_bar_callback(CALLBACK cb);
}
