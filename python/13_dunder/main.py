
class A():
    def __new__(cls, *args, **kwargs):
        print("A.__new__ called")
        return super().__new__(cls)
    
    def __init__(self, v: int = 0):
        self.__value = v
        self.__current = 0
        print("A.__init__ called")
        
    def __str__(self):
        return f"A.__str__ called {self.__value}"
    
    def __repr__(self):
        return "A()"
    
    def __eq__(self, other):
        return self.__value == other.__value
    
    def __hash__(self):
        return hash(self.__value)
    
    def __lt__(self, other):
        return self.__value < other.__value
    
    def __bool__(self):
        return self.__value != 0
    
    def __format__(self, format_spec):
        return "A.__format__ called"
    
    def __del__(self):
        print("A.__del__ called")
        
    def __len__(self):
        return self.__value
    
    def __getitem__(self, key):
        return self.__value
    
    def __setitem__(self, key, value):
        self.__value = value
    
    def __delitem__(self, key):
        self.__value = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__current > self.__value:
            raise StopIteration
        else:
            self.__current += 1
            return self.__current - 1
        
    def __contains__(self, item):
        return item == self.__value
    
    def __reversed__(self):
        return A(-self.__value)
    
    def __add__(self, other):
        if isinstance(other, int):
            return A(self.__value + other)
        elif isinstance(other, A):
            return A(self.__value + other.__value)
        else:
            raise TypeError
    
    def __getattr__(self, attr_name): # fallback for missing attributes
        print(f"A.__getattr__ called with {attr_name}")
        return None
    
    def __setattr__(self, attr_name, value):
        print(f"A.__setattr__ called with {attr_name} = {value}")
        super().__setattr__(attr_name, value)
a = A()
print(a)
b = eval(repr(a))
c = A(v=5)
print(b)
print(a == b)
print(a is b)

import pdb; pdb.set_trace()
s = set()
s.add(a)
s.add(b)
print(s)

breakpoint()
print(a < c)

print(f"{a}")

a["lofasz"] = 8
print(a)

print(a["hurka"])

del a["kolbi"]
print(a)

a[""] = 10

for v in a:
    print(v)
    
if 10 in a:
    print("10 is in a")
if 9 in a:
    print("9 is in a")

print(reversed(a))

print(a + 1)

print(a.x)

a.x = 6
print(a.x)