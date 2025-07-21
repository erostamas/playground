from abc import ABC, abstractmethod
from enum import Enum, auto

class Job(ABC):
    class Status(Enum):
        IDLE = auto()
        SUCCESS = auto()
        ERROR = auto()
        RUNNING = auto()
    
    def __init__(self, name):
        self._name = name
        self._status = Job.Status.IDLE

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    async def async_run(self):
        pass
    
    @abstractmethod
    def kill(self):
        pass

    @abstractmethod
    def info(self):
        pass
    