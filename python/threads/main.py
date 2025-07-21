import threading
import time
from abc import ABC, abstractmethod

class Job(ABC):
    
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def run(self):
        pass

class SleepJob(Job):
    def __init__(self, name, duration):
        self.__duration = duration
        super().__init__(name)

    def run(self):
        time.sleep(self.__duration)
        
    
def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")

threads = [threading.Thread(target=worker) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
