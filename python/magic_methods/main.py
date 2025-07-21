class Demo():
    def __new__(cls, *args, **kwargs):
        print(f"__new__ called {args}")
        return super().__new__(cls)
    
    def __init__(self, *args, **kwargs):
        print(f"__init__ called {args}")


d = Demo(1,2,3)