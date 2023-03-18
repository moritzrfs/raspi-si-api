from fastapi import FastAPI, HTTPException, Depends, Header, File, UploadFile
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN

app = FastAPI()

# Example API key used for authentication
API_KEY = "696969"

# Define a security scheme to handle API key authentication
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# Define a function to verify the API key
async def api_key_verification(api_key_header: str = Depends(api_key_header)):
    if api_key_header is None or api_key_header != API_KEY:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid API key")
    return api_key_header

# Define a route that requires API key authentication
@app.get("/protected")
async def protected_route(api_key: APIKey = Depends(api_key_verification)):
    return {"message": "This route is protected"}

# Define a public route
@app.get("/")
async def public_route():
    return {"message": "This route is public"}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), api_key: APIKey = Depends(api_key_verification)):
    contents = await file.read()
    return {"filename": file.filename, "contents": contents}