import os

from fastapi import FastAPI
from db_config import engine
from module_manager import ModuleManager

# Create the main FastAPI application instance.
app: FastAPI = FastAPI()
"""
The main FastAPI application instance.

Used to register routes and middleware and to serve the application.
"""

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