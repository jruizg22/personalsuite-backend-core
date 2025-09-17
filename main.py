import os

from fastapi import FastAPI
from db_config import engine
from module_manager import ModuleManager

app: FastAPI = FastAPI()

manager = ModuleManager(app, engine)
manager.load_modules()
manager.register_modules()

@app.get("/")
async def root():
    return {"message": "Hello World"}

UVICORN_HOST = os.getenv("UVICORN_HOST", "127.0.0.1")

try:
    UVICORN_PORT = int(os.getenv("UVICORN_PORT", "8000"))
except ValueError:
    raise RuntimeError(f"UVICORN_PORT must be an integer, got: {os.getenv('UVICORN_PORT')}")

UVICORN_RELOAD = os.getenv("UVICORN_RELOAD", "true").lower() in "true"

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run("main:app",
                    host=UVICORN_HOST,
                    port=UVICORN_PORT,
                    reload=UVICORN_RELOAD
                    )
    except Exception as e:
        raise RuntimeError(f"Failed to start Uvicorn server: {e}")