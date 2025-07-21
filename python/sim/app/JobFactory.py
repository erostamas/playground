import logging

class UnknownJob(Exception):
    pass

class JobFactory():
    logger = logging.getLogger(__name__)
    registry = {}
    
    def register_job(job_type: str):
        def decorator(cls):
            JobFactory.logger.info(f"Registering job type '{job_type}' - {cls.__name__}")
            JobFactory.registry[job_type] = cls
            return cls
        return decorator

    def create_job(job_data: dict):
        job_type = job_data["type"]
        if job_type not in JobFactory.registry:
            raise UnknownJob(f"Unknown job type: {job_type}")
        else:
            return JobFactory.registry[job_type].from_dict(job_data)