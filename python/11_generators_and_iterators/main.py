"""
iterators: __iter__(self) and __next__(self), next raises StopIteration
"""
class PingPong():
    def __init__(self):
        self.__dir = 1
        self.__container = [1, 2, 3, 4, 5]
        self.__current_index = 0
        print('New object created')
    
    def __iter__(self):
        return self
        
    def __next__(self):
        next_index = self.__current_index + self.__dir
        if next_index == -1 or next_index == len(self.__container):
            self.__dir *= -1
        ret = self.__container[self.__current_index]
        self.__current_index += self.__dir
        return ret

#generators yield gives control back to caller, use when lazy iteration is needed
def count_to(n):
    i = 0
    while i < n:
        i += 1
        yield i

def main():
    #mp = PingPong()
    mp = count_to(5)
    for i in mp:
        print(i)
    
    

if __name__ == '__main__':
    main()