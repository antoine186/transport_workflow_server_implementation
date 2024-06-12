# transport_workflow_server_implementation

# !!! Important:

The 3rd party server provided has been slightly modified to make my entire setup work.
Please do not use the 3rd party server sent over to me for testing. Use the 3rd party server found in this repo instead and follow the below instructions.

# A couple of considerations for testing

Given that the 3rd party server isn't straightforward to test, it is worth temporarily doing the following in order to see an entire worflow run:
* In server.py in flask_base_server, replace line 25 with "start_hour = 9". You then must time the collectionTime from the API tester to be between the time window generated.
* In server.py in flask_base_server at line 192, you won't see a landing confirmation unless you invert the < condition.

# Tradeoffs in my implementation:

The job workflow kick-off is supposed to be async and the API endpoint is not supposed to hang. The endpoint is supposed to immediately return.
These two requirements are somewhat conflicting as async will normally make the endpoint wait either when using "await" or "asyncio.run()".

Instead we made the endpoint kick-off a new separate thread each time it needs to trigger the workflow. This achieves concurrency normally found in async programming.
Additionally, during the 2 polling phases of this task, we manually make the code wait as it polls the 3rd party service, thus mimicking the "await" feature of async programming.

Trading off a purely async approach for an async one + a threaded one allows us to get the best of both worlds: async and an endpoint that returns immediately irrespective of workflow running time.

This is even more sound as the underlying workflow only changes backend values and writes to files in the backend.

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
