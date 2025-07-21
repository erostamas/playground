import pytest

from app.JobStore import JobStore, JobAlreadyExists
from app.Job import Job
from app.JobFactory import JobFactory

@JobFactory.register_job("dummy_job")
class DummyJob(Job):
    def __init__(self, name: str, number: int):
        super().__init__(name)
        self.number = number

    def run(self):
        pass
    
    def kill(self):
        pass
    
    def info(self):
        return {"type": "dummy"}
    
@pytest.fixture(autouse=True)
def reset_jobstore():
    store = JobStore()
    print("setup")
    yield store
    print("clear")
    store.clear()

def test_register_job_success():
    store = JobStore()
    job = DummyJob("kolbasz", 5)
    store.register_job(job)
    assert "kolbasz" in store.jobs
    assert store.jobs["kolbasz"] == job

def test_register_job_conflict():
    store = JobStore()
    job = DummyJob("kolbasz", 5)
    store.register_job(job)
    with pytest.raises(JobAlreadyExists) as exc:
        store.register_job(job)
    assert "kolbasz" in str(exc)

def test_jobs_immutable():
    store = JobStore()
    job = DummyJob("kolbasz", 5)
    store.register_job(job)
    jobs = store.jobs
    del jobs["kolbasz"]
    assert "kolbasz" in store.jobs

def test_singleton():
    store1 = JobStore()
    store2 = JobStore()
    assert store1 == store2
    store1.register_job(DummyJob("kolbasz", 5))
    assert "kolbasz" in store2.jobs
    
    
    