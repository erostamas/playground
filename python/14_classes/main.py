class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class F():
    def show(self):
        print("F")

class D(B, C):
    def show(self):
        super().show()
        print("D")

class E(D, F):
    def show(self):
        super().show()
        print("E")

d = E()
d.show()
print(E.mro())


class Repr:
    def __init__(self, a: int):
        self.a = a
    
    def __repr__(self):
        return f"Repr({self.a})"

    def show(self):
        print("Repr")

r = Repr(5)
print(repr(r))


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("woof")

class Corgi(Dog):
    def speak(self):
        print("I am a Corgi")

a = Dog()
a.speak()

class C:
  dangerous = 2
c1 = C()
c2 = C()
print(c1.dangerous)
c1.dangerous = 3
print (c1.dangerous)
print (c2.dangerous)
del c1.dangerous
print (c1.dangerous)
C.dangerous = 3
print (c2.dangerous)

class X():
    a = 5
    
    def __init__(self):
        pass


x = X()
print(X.__dict__)
print(x.__dict__)

x.a = 6

print(X.__dict__)
print(x.__dict__)

print(x.a)
print(X.a)

print(x.__class__.__dict__)

class O():
    @classmethod
    def f(cls):
        print(cls)
        
    @staticmethod
    def print_hello():
        print("hello")