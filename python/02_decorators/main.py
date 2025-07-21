import functools

#typical use cases:
#logging
#counting fn calls e.g. flask endpoint stat
#timing, perf measurement
#access control
#input validation
#retry logic 
#function decorator
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("I decorate")
        func(*args, **kwargs)
    return wrapper

@decorator
def fn(a):
    print(f"I am fn {a}")

fn(3)


#function decorator with argument

def print_number_before(n: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(n)
            func(*args, **kwargs)
        return wrapper
    return decorator

@print_number_before(4)
def fn2(a):
    print(f"I am fn2 {a}")

fn2(3)

#class decorator is level 1 if no params and returns cls!!!!!! just like fn decorator must call fn if it does not want to shadow

#level 1

def print_class_name(cls):
    print(f"new class name: {cls.__name__}")
    return cls

@print_class_name
class X():
    pass

#level 2
def print_class_name_and_something(something: str):
    def print_class_name(cls):
        print(f"new class name: {cls.__name__} and {something}")
        return cls
    return print_class_name

@print_class_name_and_something("hellobello")
class Y():
    pass
