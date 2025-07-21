"""
      A
     / \
    B   C
     \ /
      D

[D] + merge(MRO(B), MRO(C), [B, C])

MRO(A) = A


MRO(B) = B, A
MRO(C) = C, A
B, C

Look at the heads: B (from MRO(B)), C (from MRO(C)), B (from [B, C])

B is not in the tail of any list → ✅ Add B to MRO

Remove B from lists
A
C, A
C

C is not in the tail of any list → ✅ Add C to MRO

A
A


D, B, C, A
"""



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
print(D.__mro__)

