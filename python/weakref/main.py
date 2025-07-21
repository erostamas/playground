from collections import defaultdict
import weakref
import sys


class MyObj():
    x = 5

# refcount of builtin types can be huge because of keeping small numbers in an object cache
x = 5
y = x
#print(sys.getrefcount(x))

# if it is nomrla ref, deleting a will not cause errors in printing b
# if it is weakref, deleteing a will cause the gc to collect object so b() will be nonetype
a = MyObj()
b = weakref.ref(a)
#b = a

print(sys.getrefcount(a))

print(b().x)

del a

print(b().x)

# Use weakref when you want to refer to an object without extending its lifetime.
