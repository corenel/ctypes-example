from __future__ import print_function

import ctypes
import os


class Foo(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int), ("msg", ctypes.c_char_p)]


def test_foo():
    # load the library
    lib_path = os.path.join(os.getcwd(), os.pardir, "build", "libctypes_example.so")
    lib = ctypes.CDLL(lib_path)

    # set up the function signature
    lib.foo.argtypes = [ctypes.POINTER(Foo)]
    lib.foo.restype = ctypes.c_int

    # create a new Foo object
    foo = Foo()
    foo.value = ctypes.c_int(42)
    foo.msg = ctypes.c_char_p(b"Hello, World!")
    print("initial foo.value in Python: {}".format(foo.value))
    print("initial foo.msg: {} in Python".format(foo.msg))

    # call the function
    print("Calling foo() in Python")
    ret = lib.foo(ctypes.pointer(foo))
    print("Return value in Python: {}".format(ret))


def test_bar():
    # load the library
    lib_path = os.path.join(os.getcwd(), os.pardir, "build", "libctypes_example.so")
    lib = ctypes.CDLL(lib_path)

    # set up the function signature
    lib.bar.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_char_p]
    lib.bar.restype = ctypes.c_int

    # create variables
    bar_value = ctypes.c_int(42)
    bar_msg = ctypes.c_char_p(b"Hello, World!")
    print("initial value in Python: {}".format(bar_value.value))
    print("initial msg: {} in Python".format(bar_msg.value))

    # call the function
    print("Calling bar() in Python")
    ret = lib.bar(ctypes.pointer(bar_value), bar_msg)
    print("Return value in Python: {}".format(ret))


def test_callback():
    def callback(len_buf, buf):
        print("Callback called in Python")
        print("-> len_buf received in Python: {}".format(len_buf.contents.value))

        new_msg = "Hello, World!"
        for i in range(len(new_msg)):
            buf[i] = new_msg[i].encode("utf-8")
        buf[len(new_msg)] = b"\0"
        len_buf.contents.value = len(new_msg)

        print("-> len_buf modified in Python {}".format(len_buf.contents.value))
        print("-> buf modified in Python: {}".format(new_msg))

        if len_buf == 0:
            return 0
        else:
            return 1

    # construct the callback function
    CB_FUNC = ctypes.CFUNCTYPE(
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_int),
        # ctypes.c_char_p
        ctypes.POINTER(ctypes.c_char),
    )
    cb_func = CB_FUNC(callback)

    # load the library
    lib_path = os.path.join(os.getcwd(), os.pardir, "build", "libctypes_example.so")
    lib = ctypes.CDLL(lib_path)

    # set up the function signature
    lib.register_bar_callback.argtypes = [CB_FUNC]
    lib.register_bar_callback.restype = ctypes.c_int

    # call the function
    print("Calling register_bar_callback() in Python")
    ret = lib.register_bar_callback(cb_func)
    print("Return value in Python: {}".format(ret))


def main():
    # print("=== Running test_foo() in Python ===")
    # test_foo()
    # print("=== Running test_bar() in Python ===")
    # test_bar()
    print("=== Running test_callback() in Python ===")
    test_callback()


if __name__ == "__main__":
    main()
