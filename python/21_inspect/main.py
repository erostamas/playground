import inspect

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

sig = inspect.signature(greet)
print(sig)  
# Output: (name, greeting='Hello')


print(inspect.getsource(greet))


print(inspect.isfunction(greet))   # True
print(inspect.ismethod(greet))     # False
print(inspect.isclass(greet))      # False


def a():
    b()

def b():
    import inspect
    for frame_info in inspect.stack():
        print(frame_info.function)

a()

def foo(x, y):
    import inspect
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    print(f"Arguments: {[(arg, values[arg]) for arg in args]}")

foo(10, 20)
# Output: Arguments: [('x', 10), ('y', 20)]
