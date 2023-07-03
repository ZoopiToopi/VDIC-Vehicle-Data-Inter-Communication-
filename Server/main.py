# Set-ExecutionPolicy Unrestricted -Scope Process

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"server started successfully"}