from functools import wraps
import asyncio
import os

def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with args: {args}, kwargs: {kwargs}")
        func(*args, **kwargs)
    return wrapper

@print_args
def fn(a: int):
    print(f"fn")

@print_args
def fn2(a: str, b: str, *, c: int):
    print(f"fn2")

fn(5)
fn2("a", "b", c=9)

def register_class(cls):
    print(f"registering class {cls.__name__}")
    return cls

@register_class
def X():
    pass

@register_class
def Y():
    pass



l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubles = map(lambda x: x*2, l)
print(list(doubles))

global x
x = "global"

def outer():
    x = "outer"
    print(x)
    
    def inner():
        x = "inner"
        print(x)
    inner()

outer()

#class MyHashable():
#    def __init__(self, value):
#        self.value = value

class MyHashable():
    def __init__(self, value):
        self.value = value
    
    def __hash__(self):
        return self.value
    
    def __eq__(self, other):
        return self.value == other.value

v1 = MyHashable(5)
v2 = MyHashable(6)
v3 = MyHashable(5)
d = {}
d[v1] = 6
d[v2] = 7
d[v3] = 8

print(d)

mylist = [v for k, v in d.items()]
print(mylist)

mydict = {k.value : v for k, v in d.items()}
print(mydict)

myset = {v for k, v in d.items()}
print(myset)

def knight_rider(n: int):
    pos = -n
    dir  = 1
    while True:
        next_pos = pos + dir
        if next_pos == n or next_pos == -n:
            dir = -dir
        pos = next_pos
        yield pos

#for pos in knight_rider(5):
#    print(pos)


class KnightRider():
    def __init__(self, n):
        self.n = n
        self.pos = -n
        self.dir = 1

    def __iter__(self):
        return self

    def __next__(self):
        next_pos = self.pos + self.dir
        if next_pos == self.n or next_pos == -self.n:
            self.dir = -self.dir
        self.pos = next_pos
        return self.pos

k = KnightRider(7)

#for v in k:
#    print(v)

import asyncio
import os

async def file_exists(fname):
    while fname not in os.listdir():
        print(f"{fname} not there yet")
        await asyncio.sleep(1)
    return f"{fname} found"


async def asyncmain():
    tasks = [
        file_exists("x.txt"),
        file_exists("y.txt")
    ]

    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(asyncmain())