# *args and **kwargs
# args is a tuple, kwargs is a dict
# to pass them on, use *args and **kwargs
# * unpacks any list or tuple into positional arguments
# ** unpacks any dict into keyword arguments
# keyword only arguments come after * or *args

# here greeting will be keyword only
def lulu(a, b=2, *, c, d=4):
    print(f"{d}")

lulu(1, c=3) #works
lulu(1, 2, 3, 4) #TypeError

def decorator(func):
    def wrapper(*args, **kwargs):
        print('i am wrapper')
        return 8
    return wrapper

def run_twice(func):
    def twice_runner(*args, **kwargs):
        func(args, kwargs)
        func(args, kwargs)
    return twice_runner


@run_twice
@decorator
def add(a: int, b: int) -> int:
    return a + b

def increase(x: int):
    x += 1

def mod_dict(d: dict):
    d['been'] = 'here'

def fn(*args, **kwargs):
    print("hello from fn")
    print(f"args: {args} {type(args)}")
    for a in args:
        print(a)
    print(f"kwargs: {kwargs}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
        

def main():
    print('hello')
    print(add(3,2))
    a = 1
    increase(a)
    print(a)
    b = {'a' : 1}
    mod_dict(b)
    print(b)
    fn(4, 56, a, thevalue=5)


if __name__ == '__main__':
    main()