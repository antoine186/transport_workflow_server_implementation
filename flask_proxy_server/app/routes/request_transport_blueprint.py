from flask import Blueprint, request, make_response
import json

request_transport_blueprint = Blueprint('request_transport_blueprint', __name__)

@request_transport_blueprint.route('/api/request-transport', methods=['POST'])
def request_transport():
    payload = request.data
    payload = json.loads(payload)

    #!!!!

    operation_response = {
        "operation_success": True,
        "responsePayload": {
            #!!!!
        }
    }
    response = make_response(json.dumps(operation_response))
    return response