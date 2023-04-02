from fastapi import FastAPI, HTTPException, Depends, Header, File, UploadFile
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN
import os
import asyncio
import subprocess
from utils.kill_proc import kill_proc
from utils.start_proc import start_proc

'''
Start with the following command:
uvicorn main:app --reload
'''

app = FastAPI()
API_KEY = os.environ.get("API_KEY")
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def api_key_verification(api_key_header: str = Depends(api_key_header)):
    if api_key_header is None or api_key_header != API_KEY:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid API key")
    return api_key_header

@app.get("/protected")
async def protected_route(api_key: APIKey = Depends(api_key_verification)):
    return {"message": "This route is protected"}

@app.get("/")
async def public_route():
    return {"message": "This route is public"}

@app.get("/var/")
async def get_var():
    return os.environ.get("ANOTHER_VAR")

@app.post("/start/")
async def start_robot(api_key: APIKey = Depends(api_key_verification)):
    await start_proc('called_script.py')
    return {"message": "Robot started."}

@app.post("/stop/")
async def stop_robot(api_key: APIKey = Depends(api_key_verification)):
    if kill_proc('called_script.py'):
        return {"message": "Robot stopped."}
    else:
        return {"message": "Robot not running."}

# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile | None = None, api_key: APIKey = Depends(api_key_verification)):
#     if not file:
#         return {"message": "No upload file sent"}
#     else:
#         file_path = os.getcwd() + '/' + file.filename
#         with open(file_path, "wb") as buffer:
#             buffer.write(await file.read())
#         return {"filename": file.filename}