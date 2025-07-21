
#LEGB - Local, Enclosing, Global, Builtin

x = 'global'

def outer():
    x = 'enclosing'
    
    def inner():
        x = 'local'
        print(x)  # Prints 'local'
    
    inner()
    print(x)  # Prints 'enclosing'

outer()
print(x)      # Prints 'global'


y = 10

def modify_global():
    global y
    y = 20  # modifies the global x

modify_global()
print(y)  # Output: 20


#nonlocal to address variables in enclosing but not global scope

def outer():
    x = 'enclosing'

    def inner():
        nonlocal x
        x = 'local'
        print(x)  # Prints 'local'

    inner()
    print(x)  # Prints 'local'

outer()

#python uses lexical scoping with LEGB rule, not dynamic scoping
#Even if a function is called from somewhere else, it remembers the variables from its defining environment.
