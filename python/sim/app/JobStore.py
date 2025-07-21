"""
Defines the job store class, a singleton for thread safe storage of Jobs
"""

import threading
import logging
from app.Job import Job
from concurrent.futures import ThreadPoolExecutor
import asyncio


class JobAlreadyExists(Exception):
    """Exception reaised when attempting to register a job with a name that already exists in the store"""
    pass

class JobStore():
    """Singleton class that manages job registrations"""
    __instance = None
    __lock = threading.Lock()
    __logger = logging.getLogger(__name__)
    __threads = {}
    __executor = ThreadPoolExecutor(max_workers = 3)
    __futures = {}
    __tasks = {}

    def __new__(cls):
        with JobStore.__lock:
            if not cls.__instance:
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if getattr(self, '_initialized', False):
            return
        self.__jobs = {}
        self._initialized = True
        def start_loop(loop):
            asyncio.set_event_loop(loop)
            loop.run_forever()
        self._eventloop = asyncio.new_event_loop()
        threading.Thread(target=start_loop, args=(self._eventloop,), daemon=True).start()
        

    @property
    def jobs(self):
        """
        Returns a shallow copy of the currently registered jobs
        
        Returns:
            dict: a dictionary of job name -> job object
        """
        return dict(self.__jobs)
    

    def register_job(self, new_job: Job):
        """
        Registers a new job if it does not already exists
        
        Args:
            new_job (Job): a Job instance to register
        
        Raises:
            JobAlreadyExists: If a job with the same name already exists
        """
        new_job_name = new_job.name
        self.__logger.info(f"Trying to register job '{new_job_name}'")
        with JobStore.__lock:
            if new_job_name not in self.__jobs:
                self.__jobs[new_job_name] = new_job
                #with simple threads
                #new_thread = threading.Thread(target=self.__jobs[new_job_name].run)
                #self.__threads[new_job_name] = new_thread
                #new_thread.start()
                #with threadpoolexecutor
                #self.__futures[new_job_name] = self.__executor.submit(self.__jobs[new_job_name].run)
                #with asyncio
                self.__tasks[new_job_name] = asyncio.run_coroutine_threadsafe(new_job.async_run(), self._eventloop)
            else:
                raise JobAlreadyExists(f"Job with name: '{new_job_name}' already exists")
    
    def clear(self):
        """
        Clears all the job registrations
        """
        with JobStore.__lock:
            self.__jobs.clear()

    def info(self):
        with JobStore.__lock:
            ret = {}
            for name, job in self.__jobs.items():
                ret[name] = job.info()
                ret[name]["status"] = job.status.name
                #ret[name]["future"] = self.__futures[name].done()
            return ret
            
        
        