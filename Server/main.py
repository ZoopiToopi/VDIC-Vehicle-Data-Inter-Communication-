# Set-ExecutionPolicy Unrestricted -Scope Process

from  fastapi import FastAPI
import subprocess

app = FastAPI()

run_once = 1
port = 5050
ngrok = "ngrok.exe http "+str(port)
# date = "date"
while 1:
    if run_once == 1: 
        print("starting ngrok server.......")
        os_data = subprocess.Popen('start cmd /c'+ngrok)
        print(os_data.decode("utf-8"))
        run_once = 0
        
    # os.system()
    @app.get("/")
    async def root():
        return {"server started successfully"}
    @app.get("/request/{request_dat}")
    async def name_func(request_dat):
        return {"you have sent this to us : "+ request_dat}