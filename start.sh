#!/bin/sh

PORT=$PORT
if [ -z "$PORT" ]; then PORT=8000; fi

# Just start the server (no training)
uvicorn app.main:app --host 0.0.0.0 --port $PORT