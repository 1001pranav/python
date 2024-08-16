# FAST API

To run the fast API server, run the following command:
`uvicorn server:app --reload`

Where -
    `server` is the file containing the FastAPI app.
    `app` refers to the object inside the `server.py` file
    `--reload` is the flag to reload the app when changes are made.

By Default the endpoint for the FastAPI is - `http://127.0.0.1:8000/`,

To change the port  add `--port <PORT_NUMBER>` flag in the above command.

If You want to change the host then we can use `--host <HOST_NAME>` flag.