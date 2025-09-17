import os

from sqlalchemy import Engine
from sqlmodel import create_engine

# Retrieve the database URL from the environment variable.
DATABASE_URL: str = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not defined")
"""
The URL of the database to connect to.

This value is retrieved from the environment variable 'DATABASE_URL'.
Raises a RuntimeError if the environment variable is not defined.
As the application isn't intended to run without a database, the raise prevents the app from starting.
"""

# Determine whether SQLAlchemy should echo SQL statements.
ENGINE_ECHO: bool = os.getenv("ENGINE_ECHO", "false").lower() in "true"
"""
Flag indicating if the SQLAlchemy engine should log all SQL statements.

- True: SQL statements will be printed to stdout.
- False: SQL statements will not be printed.

This is controlled by the 'ENGINE_ECHO' environment variable.
"""

# Create the SQLAlchemy engine using the database URL and echo flag.
engine: Engine = create_engine(DATABASE_URL, echo=ENGINE_ECHO)
"""
The SQLAlchemy engine instance used to interact with the database.

Args:
    DATABASE_URL (str): The connection URL for the database.
    echo (bool): If True, SQL statements will be echoed to the console.
"""