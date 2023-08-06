Set-ExecutionPolicy Unrestricted -Scope Process -----> to execute script in power shell
uvicorn main:app --reload --port 5050 --------> uvicorn server up
ngrok http 5050 (here 5050 is the port. we can change to available port)