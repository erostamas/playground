#small throwaway function

#map: apply lambda for each element in an iterable

#filter: keep those in a n iterable for which lambda returned true

#reduce: apply lambda cumulatively (((a, b), c), d)

add10 = lambda x: x + 10
print(add10(5))

multiply = lambda x, y: x * y
print(multiply(5,6))

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)

num = [1, 2, 3]
themap = map(lambda x: x**2, num)
print(themap)
squares = list(map(lambda x: x**2, num))
print(squares)

numbers = [1,2,3,4,5,6,7,8]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

from functools import reduce
factorial = reduce(lambda x, y: x * y, numbers)
print(factorial)