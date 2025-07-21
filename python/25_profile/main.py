import time

def a():
    print("a start")
    time.sleep(5)
    print("a done")

def b():
    print("b start")
    time.sleep(1)
    print("a done")
    

a()
b()
b()
b()

"""
python3 -m cProfile main.py 
a start
a done
b start
a done
b start
a done
b start
a done
         19 function calls in 8.001 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.001    8.001 {built-in method builtins.exec}
        1    0.000    0.000    8.001    8.001 main.py:1(<module>)
        4    8.001    2.000    8.001    2.000 {built-in method time.sleep}
        1    0.000    0.000    5.000    5.000 main.py:3(a)
        3    0.000    0.000    3.001    1.000 main.py:8(b)
        8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


"""
line profiler
python3 -m pip install line_profiler

works with a decorator @profile
"""

@profile
def slow_function():
    total = 0
    for i in range(10000):
        for j in range(100):
            total += i * j
    return total

if __name__ == "__main__":
    slow_function()
    
"""
kernprof -l -v ./main.py 
a start
a done
b start
a done
b start
a done
b start
a done
Wrote profile results to main.py.lprof
Timer unit: 1e-06 s

Total time: 0.659339 s
File: ./main.py
Function: slow_function at line 51

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    51                                           @profile
    52                                           def slow_function():
    53         1          2.0      2.0      0.0      total = 0
    54     10001       2638.5      0.3      0.4      for i in range(10000):
    55   1010000     274457.4      0.3     41.6          for j in range(100):
    56   1000000     382240.2      0.4     58.0              total += i * j
    57         1          0.7      0.7      0.0      return total
"""

"""
timeit for precise measurement of function times 
import timeit

code = "sum(range(1000))"
execution_time = timeit.timeit(code, number=10000)
print(f"Time: {execution_time} seconds")
"""


"""
python3 -m memory_profiler ./main.py
a start
a done
b start
a done
b start
a done
b start
a done

Filename: ./main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    51   22.434 MiB   22.434 MiB           1   @profile
    52                                         def slow_function():
    53   22.434 MiB    0.000 MiB           1       total = 0
    54   22.434 MiB    0.000 MiB       10001       for i in range(10000):
    55   22.434 MiB    0.000 MiB     1010000           for j in range(100):
    56   22.434 MiB    0.000 MiB     1000000               total += i * j
    57   22.434 MiB    0.000 MiB           1       return total
"""

