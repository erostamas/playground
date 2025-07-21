from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        """
        sets capacity
        initializes the deque that will store the keys
        initializes the dict that will store the key-value pairs
        """
        self.__capacity = capacity
        self.__values = set()
        self.__q = deque()
                
    def get(self, key: int) -> int:
        """
        Gets the value for key
        
        Args:
            key (int): the key.

        Returns:
            int: the value, or -1 if key does not exist
        """
        ret = -1
        if key in self.__values:
            self.__q.remove(key)
            ret = self.__values[key]
        self.__q.appendleft(key)
        return ret

    def put(self, key: int, value: int) -> None:
        """
        Puts a new key/value pair in
        
        Args:
            key (int): the key.
            value (int): the value.

        Returns:
            None
        """
        self.__q.appendleft(key)
        if key in self.__values:
            self.__q.remove(key)
        self.__q.appendleft(key)
        self.__values[key] = value
        if len(self.__q) > self.__capacity:
            self.__q.pop()
        

