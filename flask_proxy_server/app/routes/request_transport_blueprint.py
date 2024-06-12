from flask import Blueprint, request, make_response
import json
import threading

from app.routes.utils.request_transport_handler import request_transport_handler

request_transport_blueprint = Blueprint('request_transport_blueprint', __name__)

@request_transport_blueprint.route('/request-transport', methods=['POST'])
def request_transport():
    try:
        payload = json.loads(request.data)

        client_id = payload['clientId']
        product_id = payload['productId']
        quantity = payload['quantity']
        origin = payload['origin']
        destination = payload['destination']
        collection_time = payload['collectionTime']
        
        transport_request_params = {
            'clientId': client_id,
            'productId': product_id,
            'quantity': quantity,
            'origin': origin,
            'destination': destination,
            'collectionTime': collection_time,
        }
        
        thread = threading.Thread(target=request_transport_handler, args=(transport_request_params,))
        thread.start()

        operation_response = {
            "operation_success": True,
        }
        response = make_response(json.dumps(operation_response))
        return response
    except Exception as e:
        operation_response = {
            "operation_success": False,
            "responsePayload": {
                "error_message": str(e)
            }
        }
        response = make_response(json.dumps(operation_response))
        return response