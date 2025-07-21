"""
referenec counting, if count is 0, object is deallocated

cyclic refs, where object ref each other and count will not drop to 0, are collected by GC, cyclic garbage collector
this can be called maunally with gc.collect()
"""

import sys

class MyClass:
    def __del__(self):
        print("MyClass instance deleted")

obj = MyClass()
print("Ref count:", sys.getrefcount(obj))  # +1 due to getrefcount() argument

del obj  # Ref count drops to 0, triggers __del__()



# Cyclic ref
import gc

class Node:
    def __init__(self):
        self.ref = None
    def __del__(self):
        print("Node deleted")

# Create two nodes referencing each other (cycle)
a = Node()
b = Node()
a.ref = b
b.ref = a

# Remove external references
del a
del b

# At this point, objects are unreachable but not deleted yet
print("Collecting garbage...")
gc.collect()  # Manually trigger collection of cyclic garbage
