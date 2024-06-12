import requests
from config import flask_base_server_url
import json

def request_job(transport_request_params):
    response = requests.post(flask_base_server_url + '/carrier/request-job', json=transport_request_params)
    
    return json.loads(response.text)
