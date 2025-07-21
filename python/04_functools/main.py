import functools

def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")

    return wrapper

@decorator
def x():
    pass

print(x.__name__) # print wrapper

def decorator2(func):
    @functools.wraps(func) # wraps keeps the func identity
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")

    return wrapper

@decorator2
def y():
    pass

print(y.__name__)


#partial creates a new version oif a function with some arguments fixed\

def f(a, b):
    return a * b

double = functools.partial(f, b=2)

print(double(2))


#functools.lru_cache

# Automatically caches results of function calls based on arguments, to speed up repeated calls.

@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))  # Much faster with caching, fib(5) calls fib(4) and fib(3) and also fib(4) calls fib(3) so it spares a call to each fn