"""
getattr gets an attribute of an object and raises attributerror if does not exist
"""

class Person:
    def __init__(self):
        self.name = "Alice"
    def x(a: int):
        return 7

p = Person()

print(getattr(p, 'name'))         # → "Alice"
print(getattr(p, 'age', 30))      # → 30 (uses default)
print(p.__dict__)


"""
setattr sets an attribute of an object
"""

setattr(p, 'age', 25)             # p.age = 25
print(p.age)                      # → 25


"""
hasattr checks if an attribute exists
"""

print(hasattr(p, 'name'))         # → True

"""
dir
Returns a list of all (or most) attribute names of the object, including methods and dunder methods.
"""

print(dir(p))