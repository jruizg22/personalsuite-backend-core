import os
from sqlmodel import create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not defined")

ENGINE_ECHO = os.getenv("ENGINE_ECHO", "false").lower() in "true"

engine = create_engine(DATABASE_URL, echo=ENGINE_ECHO)