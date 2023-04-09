from fastapi import FastAPI, HTTPException, Depends, Header, File, UploadFile, Request
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN
import os
import json
from typing import Union
from utils.call_robot import action
import threading

from utils.proc_actions import start_proc, kill_proc, is_process_running
from utils.call_shell import run_command
'''
Start with the following command:
uvicorn main:app --reload
'''

app = FastAPI()

API_KEY = os.environ.get("API_KEY")
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
stop_flag = False
robot = None

async def api_key_verification(api_key_header: str = Depends(api_key_header)):
    if api_key_header is None or api_key_header != API_KEY:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid API key")
    return api_key_header



@app.post("/start/")
async def start_robot(api_key: APIKey = Depends(api_key_verification)):
    """
    Start the robot if it is not already running.

    This endpoint will start the robot if it is not already running.
    If it is already running, it will return a message saying so.
    If it is not running, it will start the robot and return a message saying so.
    """
    t = threading.Thread(target=action)
    t.start()
    return {"message": "Robot started."}

@app.post("/my_endpoint")
async def my_endpoint(request: Request):
    body = await request.json()
    my_value = body.get("my_value")
    return {"message": f"Received request body. My value is: {my_value}"}


@app.post("/shell/")
async def exec_shell(request: Request, api_key: APIKey = Depends(api_key_verification)):
    """
    Triggers a shell command.
    Body needs to have a "command" key with 
    the command to be executed as value.
    """
    body = await request.json()
    if 'command' in body:
        message = run_command(body['command'])
        return {"message": message}
    else:
        return {"message": "No command sent."}


@app.post("/shell2/")
async def exec_shell2(request: Request):
    """
    Triggers a shell command.
    Body needs to have a "command" key with 
    the command to be executed as value.
    """
    body = await request.json()
    if 'command' in body:
        command_list = body['command'].split()
        message = run_command(command_list)
        return {"message": message}
    else:
        return {"message": "No command sent."}

@app.post("/stop/")
async def stop_robot(api_key: APIKey = Depends(api_key_verification)):
    """
    Stop the robot if it is running.

    This endpoint will stop the robot if it is running.
    If it is not running, it will return a message saying so.
    If it is running, it will stop the robot and return a message saying so.
    """
    global stop_flag
    stop_flag = True
    return {"message": "Robot stopped."}

@app.get("/status/")
async def get_status(api_key: APIKey = Depends(api_key_verification)):
    """
    Get the status of the robot.
    
    This endpoint will return a message saying if the robot is running or not.
    """
    if is_process_running('called_script.py'):
        return {"message": "Robot running."}
    else:
        return {"message": "Robot not running."}
    

# @app.post("/uploadfile/")
# async def create_upload_file(file: Union[UploadFile, None] = None, api_key: APIKey = Depends(api_key_verification)):
#     if not file:
#         return {"message": "No upload file sent"}
#     else:
#         file_path = os.getcwd() + '/' + file.filename
#         with open(file_path, "wb") as buffer:
#             buffer.write(await file.read())
#         return {"filename": file.filename}

@app.post("/uploadfile/")
async def create_upload_file(file: Union[UploadFile, None] = None, api_key: APIKey = Depends(api_key_verification)):
    """
    Upload a JSON driving instructions file.

    This endpoint allows to upload a JSON file containing driving instructions.
    It checks if the file is a JSON file and if it is encoded in UTF-8.
    If the file is valid, it will be saved on the endpoint device.
    """
    if not file:
        return {"message": "No upload file sent"}

    if not file.filename.endswith('.json'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only JSON files are allowed.")

    contents = await file.read()
    try:
        json.loads(contents.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(status_code=400, detail="Invalid file encoding. Only UTF-8 encoded JSON files are allowed.")

    file_path = os.getcwd() + '/' + file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(contents)
    return {"filename": file.filename}
