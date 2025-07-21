import timeit
import random
import array

NUMBER = 10000000
mylist = []
mydict = {}
myset = set()
myarray = array.array('i')

def extend_set():
    myset.add(random.randint(0, 10**6))
    
def extend_list():
    mylist.append(random.randint(0, 10**6))
    
def extend_array():
    myarray.append(random.randint(0, 10**6))
    
def measure(stmt, setup=''):
    time_taken = timeit.timeit(stmt=stmt, setup=setup, number=NUMBER)
    print(f"{stmt} took {time_taken} seconds")

def main():
    print('hello')
    measure(stmt=extend_list)
    measure(stmt=extend_set)
    measure(stmt=extend_array)


if __name__ == '__main__':
    main()
    
    
    """
    list
    tuple
    set
    frozenset
    dict
    defaultdict
    ordereddict
    deque
    heapq
    Counter
    named tuple
    from collections import namedtuple

    Point = namedtuple("Point", ["x", "y"])
    
    
    dataclass
    from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int = 0  # default value

p = Point(3)
print(p.x, p.y)       # 3 0
print(p)              # Point(x=3, y=0)
    """