#LIST
#[expression for item in iterable]
#[expression for item in iterable if condition]

nums = [1,2,3,4]
squares = [n*n for n in nums]
print(squares)

evens = [n for n in nums if n % 2 == 0]
print(evens)

#string transformations
words = ["hello", "world"]
upper_words = [w.upper() for w in words]
print(upper_words)  # Output: ['HELLO', 'WORLD']


#DICT
#{key_expr: value_expr for item in iterable if condition}
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name : len(name) for name in names}
print(name_lengths)

#swap keys and values in dict
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # Output: {1: 'a', 2: 'b', 3: 'c'}

x = [a for a in [1, 2, 3, 4,5 , 6] if a < 4]
print(x)

d = {a : 2*a for a in [1, 2, 3, 4,5 , 6] if a < 4}
print(d)

s = {a for a in [1, 2, 3, 4,5 , 6] if a < 4}
print(s)
