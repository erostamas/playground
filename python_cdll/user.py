#!/usr/bin/python3 -B

from ctypes import *

mylib = CDLL('/home/erostamas/repos/playground/python_cdll/lib/build/libmylib.so')

add = mylib.add
add.argtypes = [c_int, c_int]
add.restype = c_int
print(add(1, 2))