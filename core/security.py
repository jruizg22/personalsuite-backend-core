import os

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

# Load the API key from environment variables
# This avoids hardcoding sensitive credentials in the source code
API_KEY: str = os.getenv("PERSONALSUITE_API_KEY")
if not API_KEY:
    raise RuntimeError("PERSONALSUITE_API_KEY environment variable is not defined")

# Define the expected header name for the API key
api_key_header: APIKeyHeader = APIKeyHeader(name="X-API-Key", auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)) -> str:
    """
    Validate the incoming API key from the request header.

    Args:
        api_key (str): The value of the `X-API-Key` header extracted by FastAPI.

    Returns:
        str: The valid API key if the request is authorized.

    Raises:
        HTTPException: If the API key is missing or does not match the expected value.
    """
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API Key")
    return api_key
