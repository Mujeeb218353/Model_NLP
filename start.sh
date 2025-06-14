#!/bin/sh

# Set fallback port
PORT=$PORT
if [ -z "$PORT" ]; then PORT=8000; fi

# Train model
python -c "from app.utils import train_and_save_model; train_and_save_model()"

# Start FastAPI
uvicorn app.main:app --host 0.0.0.0 --port $PORT