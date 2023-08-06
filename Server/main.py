# Set-ExecutionPolicy Unrestricted -Scope Process

from  fastapi import FastAPI
import subprocess

app = FastAPI()

# Global Variable

port = 5050
run_once = 1
Status = False
ngrok = "ngrok.exe http "+str(port)

def ngrok_Initialize():
    print("\nstarting global server.......")
    subprocess.Popen('start cmd /c'+ngrok,shell = True)
    return Status
  
if run_once == 1: 
    Status = ngrok_Initialize()
    run_once = 0
            
# os.system()
@app.get("/")
async def root():
    return {"server started successfully"}
@app.get("/request/{request_dat}")
async def name_func(request_dat):
    return {"you have sent this to us : "+ request_dat}
@app.get("/akdata")
async def data():
    return{"ipo mariyille, ithu pole enik url api detect cheyth data share cheyyan patum"}
