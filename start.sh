#!/bin/bash

# Use port 8000 locally or $PORT on Railway
PORT=${ PORT:-8000 }

# Train model
python -c "from app.utils import train_and_save_model; train_and_save_model()"

# Start server
uvicorn app.main:app --host 0.0.0.0 --port $PORT