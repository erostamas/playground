import timeit
import time
import random
import array
import threading


def fn1():
    for i in range(15):
        time.sleep(1)
    

def fn2():
    for i in range(15):
        time.sleep(2)

@profile
def main():
    print('hello')
    t1 = threading.Thread(target=fn1)
    t2 = threading.Thread(target=fn2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()