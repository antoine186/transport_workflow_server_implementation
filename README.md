# transport_workflow_server_implementation

# How to run the setup for testing
## Please use VSCode debugging (instructions included here) as otherwise the setup might not work as intended

! flask_base_server is the 3rd party server provided as part of this task
! flask_proxy_server is the server that I built to interact with the provided 3rd party server.
You should only test flask_proxy_server.

* Install VSCode and open flask_base_server using VSCode.
* In VSCode, do CTRL+SHIFT+D. Press on the play button that appears on the left (not the one on the right).

* Separately, open flask_proxy_server using VSCode.
* Once again in VSCode, do CTRL+SHIFT+D. Press on the play button that appears on the left (not the one on the right).

* Wait until "Running on http://127.0.0.1:5000" and ""Running on http://127.0.0.1:8000"" displays in both VSCode terminals.

* Install the Postman API client
* In Postman, click the "New" button in the top left. A new request template should popup.
* Switch the template from GET to POST. Paste http://127.0.0.1:5000/request-transport in your url box.
* Below the url box is a nav bar with "body". Click that and then select "raw". Paste the below in:

{
    "clientId": 1,
    "productId": 1,
    "quantity": 1,
    "origin": "A",
    "destination": "B",
    "collectionTime": "2024-06-13T09:30:00"
}

* Press the "SEND" button and wait for Postman to display the result.
