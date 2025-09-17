FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    && python -m ensurepip --upgrade \
    && pip install --upgrade pip setuptools wheel \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /personalsuite

# Copy the core application
COPY personalsuite-backend-core/ ./core/

# Copy modules
# Example:
# COPY module-root-directory/ ./modules/modulename/

# Install global dependencies
RUN pip install --no-cache-dir fastapi[standard-no-fastapi-cloud-cli] sqlmodel psycopg2-binary uvicorn

# Install core and modules
RUN pip install ./core
# Example for installing a module:
# RUN pip install ./modules/modulename

# FastAPI runs on port 8000 by default
EXPOSE 8000

# Default command to run the FastAPI application
CMD ["python", "core/main.py"]