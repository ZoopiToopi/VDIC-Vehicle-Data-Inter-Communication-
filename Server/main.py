# Set-ExecutionPolicy Unrestricted -Scope Process

from  fastapi import FastAPI
import subprocess

app = FastAPI()

# Global Variable

port = 5080
ngrok = "ngrok.exe http "+str(port)
uvicorn = "uvicorn main:app --reload --port "+str(port)

# Global Variables end

# Private Function Prototypes

def ngrok_Initialize():
    print("\nstarting global server.......")
    subprocess.Popen('start cmd /c'+ngrok,shell = True)
    return True

def uvicorn_Initialize():
    print("\nstarting local server.......")
    subprocess.Popen('start cmd /c'+uvicorn,shell = True)
    return True
# Function prototype end



run_once = 1
Status = False

# date = "date"
while 1:
    if run_once == 1: 
        # Status = uvicorn_Initialize()
        Status = True
        # Status = ngrok_Initialize()
        run_once = 0
        # if(True == Status):
        #     Status = False
        #     Status = ngrok_Initialize()
        # if(False == Status):
        #     print("Error! Please check ngrok and uvicorn connection")
        #     break
        
    # os.system()
    @app.get("/")
    async def root():
        return {"server started successfully"}
    @app.get("/request/{request_dat}")
    async def name_func(request_dat):
        return {"you have sent this to us : "+ request_dat}
    @app.get("/akdata")
    async def data():
        return{"akhils data"}