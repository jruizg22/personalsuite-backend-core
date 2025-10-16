import os

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from db_config import engine
from module_manager import ModuleManager
from security import get_api_key
from allowed_origins import origins

# Create the main FastAPI application instance.
#
# This instance will serve as the central point for all API routes and configuration.
# The `title` parameter sets the API title shown in the documentation (/docs or /redoc).
# The `dependencies` parameter applies a global dependency: in this case, `get_api_key`.
#
# By including `Depends(get_api_key)` here, every endpoint in the application will require
# a valid API key, effectively securing the API and restricting access to authorized clients only.
app: FastAPI = FastAPI(
    title="Personal Suite",
    dependencies=[Depends(get_api_key)]
)

# Configure Cross-Origin Resource Sharing (CORS) middleware.
#
# This middleware enables the FastAPI application to handle requests from different origins,
# which is essential when the frontend (e.g., a React or Vue app) is hosted on a different domain
# or port than the backend API.
#
# The `origins` list defines the allowed origins (domains) that can make requests to this API.
# - During development, it can be set to ["*"] to allow all origins.
# - In production, it is strongly recommended to replace "*" with an explicit list of trusted domains,
#   for example:
#       origins = [
#           "https://app.personalsuite.com",
#           "https://admin.personalsuite.com"
#       ]
#
# The parameters control the CORS behavior:
# - `allow_origins`: Specifies which domains are permitted to access the API.
# - `allow_credentials`: Enables cookies, authorization headers, and other credentials.
# - `allow_methods`: Specifies which HTTP methods are allowed (e.g., GET, POST, PUT, DELETE).
#   Setting ["*"] allows all methods.
# - `allow_headers`: Defines which headers can be included in the request.
#   Using ["*"] allows any header, including custom ones like "X-API-Key".
#
# This configuration ensures that browser-based clients (e.g., frontend apps)
# can interact securely and seamlessly with the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the ModuleManager with the FastAPI app and database engine.
manager: ModuleManager = ModuleManager(app, engine)
manager.load_modules()
manager.register_modules()
"""
The ModuleManager instance responsible for loading and registering
all application modules.
"""

@app.get("/")
async def root() -> dict:
    """
    Root endpoint of the FastAPI application.

    Returns:
        dict: A simple JSON message indicating the server is running.
    """
    return {"message": "Hello World"}

@app.get("/modules")
def module_list() -> list[str]:
    return manager.list_loaded()

# Retrieve Uvicorn host configuration from environment variables.
UVICORN_HOST: str = os.getenv("UVICORN_HOST", "0.0.0.0")
"""
The host address for the Uvicorn server.

Defaults to '0.0.0.0' if the environment variable is not set, allowing access from all interfaces.
"""

# Retrieve and validate Uvicorn port configuration.
try:
    UVICORN_PORT: int = int(os.getenv("UVICORN_PORT", "8000"))
except ValueError:
    raise RuntimeError(f"UVICORN_PORT must be an integer, got: {os.getenv('UVICORN_PORT')}")
"""
The port number for the Uvicorn server.

Raises:
    RuntimeError: If the environment variable is not a valid integer.
"""

# Determine whether Uvicorn should reload on code changes.
UVICORN_RELOAD: bool = os.getenv("UVICORN_RELOAD", "true").lower() in "true"
"""
Flag indicating whether Uvicorn should automatically reload on code changes.

Defaults to True if the environment variable is not set.
"""

if __name__ == "__main__":
    """
    Entry point for running the FastAPI application with Uvicorn.

    Uses environment variables to configure host, port, and reload behavior.
    """
    import uvicorn
    try:
        uvicorn.run("main:app",
                    host=UVICORN_HOST,
                    port=UVICORN_PORT,
                    reload=UVICORN_RELOAD
                    )
    except Exception as e:
        raise RuntimeError(f"Failed to start Uvicorn server: {e}")