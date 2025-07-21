#closure is a function that remembers the variables from its enclosing scope even if that scope has finished executing

def outer(msg):
    var = 0
    def inner():
        nonlocal var # nonlocal means dont create a new local var, use the enclosing scope but not the global
        var += 1
        print(f"{msg} {var}")
    return inner

f = outer("Hello")
f() #1
f() #2
f() #3
f() #4