import requests
from config import flask_base_server_url
import json

def get_job_status(job_status_request_params):
    response = requests.get(flask_base_server_url + '/carrier/job/status', json=job_status_request_params)
    
    return json.loads(response.text)
