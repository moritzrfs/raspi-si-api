from fastapi import HTTPException
import os
import json

async def save_file(file):
    """
    Helper function to save the uploaded file.
    """
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
    return file.filename