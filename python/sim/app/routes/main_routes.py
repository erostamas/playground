from flask import Blueprint, jsonify, request
from app.JobStore import JobStore, JobAlreadyExists
import logging
from app.Statistics import Statistics
from app.JobFactory import JobFactory

main = Blueprint('main', __name__)
logger = logging.getLogger(__name__)


@main.route('/')
@Statistics.count_calls("index")
def index():
    return "hello from my sim app"


@main.route('/register_job', methods=['POST'])
@Statistics.count_calls("register_job")
def register_job():
    """
    Register a new job
    ---
    tags:
      - Jobs
    parameters:
      - name: job
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - type
          properties:
            name:
              type: string
            type:
              type: string
    responses:
      200:
        description: Job successfully registered
      409:
        description: Job already exists
    """
    job_data = request.get_json()
    logger.info(f"Job registration received: {job_data}")
    js = JobStore()
    try:
        job = JobFactory.create_job(job_data)
        js.register_job(job)
        return jsonify(job_data), 200
    except JobAlreadyExists as e:
        return jsonify({"error": str(e)}), 409
    
@main.route('/job_status', methods=['GET'])
@Statistics.count_calls("job_status")
def job_status():
    """
    Get job status
    ---
    tags:
      - Jobs
    """
    js = JobStore()
    try:
        return jsonify(js.info()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500