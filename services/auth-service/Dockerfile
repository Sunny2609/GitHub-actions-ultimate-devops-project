# -------------------------
# STAGE 1: Build environment
# -------------------------

FROM python:3.10-slim AS builder

# set working directory
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y gcc

# Install Python dependencies in a temp folder
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt


# -------------------------
# STAGE 2: Runtime environment
# ----------------------------

FROM python:3.10-slim

# Set working directory
WORKDIR /app

RUN apt-get update && apt-get install -y curl

# Copy installed Python packages from builder image
COPY --from=builder /install /usr/local

# Copy our application code
COPY app app

# Expose FastAPI port
EXPOSE 8000

# Healthcheck (Production Standard)
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1


# Start Uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

