from app.routes.utils.base_server_calling_utils.request_job import request_job
from app.routes.utils.base_server_calling_utils.get_job_status import get_job_status
from app.routes.utils.base_server_calling_utils.release_from_warehouse import release_from_warehouse
from app.routes.utils.base_server_calling_utils.get_product_status import get_product_status

import json

def request_transport_handler(transport_request_params):
    job_request_response = request_job(transport_request_params)
    
    if job_request_response['status'] == 'REJECT':
        return
    
    job_id_to_poll = job_request_response['jobId']
    job_polling = False
    
    collection_confirmation_filename = f"collection-confirmation-{job_id_to_poll}.json"
    collection_confirmation_file_content = {
        "productsId": job_id_to_poll,
        "quantity": transport_request_params['quantity'],
        "collectionTime": job_request_response['collectionTime']
    }
    with open(collection_confirmation_filename, 'w') as f:
        json.dump(collection_confirmation_file_content, f, indent=4)
        
    warehouse_release_params = {
        "productId": transport_request_params['productId'],
        "warehouseId": transport_request_params['origin'],
        "quantity": transport_request_params['quantity'],
        "collectionTime": transport_request_params['collectionTime'],
    }
    
    warehouse_release_response = release_from_warehouse(warehouse_release_params)
    
    if warehouse_release_response['status'] != 'SUCCESS':
        return
        
    job_status_response = get_job_status({"jobId": job_id_to_poll})
    
    if job_status_response['status'] == 'PENDING':
        job_polling = True
    elif job_status_response['status'] != 'RELEASED':
        return
    
    while job_polling:
        job_status_response = get_job_status({"jobId": job_id_to_poll})
    
        if job_status_response['status'] != 'PENDING':
            if job_status_response['status'] != 'RELEASED':
                return
            else:
                job_polling = False
                
    product_status_request_params = {
        "productId": transport_request_params['productId'],
        "warehouseId": transport_request_params['origin'],
    }
    
    product_status_request_response = get_product_status(product_status_request_params)
    product_polling = False
    
    if product_status_request_response['status'] == 'NOT LANDED':
        product_polling = True
    elif product_status_request_response['status'] != 'LANDED':
        return
    
    while product_polling:
        product_status_request_response = get_product_status(product_status_request_params)
    
        if product_status_request_response['status'] != 'NOT LANDED':
            if product_status_request_response['status'] != 'LANDED':
                return
            else:
                product_polling = False
                
    landing_confirmation_filename = f"landing-confirmation-{transport_request_params['destination']}-{transport_request_params['productId']}.json"
    landing_confirmation_file_content = {
        "quantity": transport_request_params['quantity']
    }
    with open(landing_confirmation_filename, 'w') as f:
        json.dump(landing_confirmation_file_content, f, indent=4)
    
    return
