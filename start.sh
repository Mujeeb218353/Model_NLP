#!/bin/bash

PORT=${PORT:-8000}
python -c "from app.utils import train_and_save_model; train_and_save_model()"
uvicorn app.main:app --host 0.0.0.0 --port $PORT