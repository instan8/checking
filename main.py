from fastapi.responses import FileResponse
from fastapi import FastAPI
import os
app=FastAPI()

@app.get("/main")
def file():
    return FileResponse("amittrivedi/darya.jpg")

   