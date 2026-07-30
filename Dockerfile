
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (required for psycopg2 and GeoAlchemy2)
RUN apt-get update \
    && apt-get install -y gcc libpq-dev gdal-bin \
    && apt-get clean

# Install Python dependencies from the backend folder
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend source code into the working directory
COPY backend/ .

# Expose port (Documentation purposes, Railway maps to $PORT dynamically)
EXPOSE 8000

# Command to run the application in production mode
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}

