"""
A metaclass is basically a “class of a class.”

Just like an object is an instance of a class, a class itself is an instance of a metaclass.

Metaclasses control how classes are created.

By default, the metaclass in Python is type.

You can create your own metaclass to customize class creation — for example, to modify attributes, enforce rules, or register classes automatically.
"""

# Define a metaclass by inheriting from 'type'
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        # Add a new attribute automatically to any class using this metaclass
        dct['custom_attr'] = 42
        return super().__new__(cls, name, bases, dct)

# Use the metaclass in a class definition
class MyClass(metaclass=MyMeta):
    pass


# Use the metaclass in a class definition
class MyOtherClass(metaclass=MyMeta):
    pass

# When MyClass is created, the metaclass __new__ runs:
print(MyClass.custom_attr)  # Output: 42
