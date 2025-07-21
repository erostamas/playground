from abc import ABC, abstractmethod
from app.Job import Job
import time
from app.JobFactory import JobFactory
import asyncio

TYPE = "sleep"
@JobFactory.register_job(TYPE)
class SleepJob(Job):
    def __init__(self, name: str, duration: int):
        super().__init__(name)
        self.__duration = duration

    @classmethod
    def from_dict(cls, job_data: dict):
        return cls(job_data['name'], job_data['options']['duration'])

    def run(self):
        print("run")
        self._status = Job.Status.RUNNING
        print(f"run status: {self.status.name}")
        time.sleep(self.__duration)
        self._status = Job.Status.SUCCESS

    async def async_run(self):
        print("async run")
        self._status = Job.Status.RUNNING
        await asyncio.sleep(self.__duration)
        print("async run done")
        self._status = Job.Status.SUCCESS
    
    def kill(self):
        print("SleepJob kill")

    def info(self):
        return {"type": TYPE, "duration": self.__duration}
    