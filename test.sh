#!/bin/sh

curl -X POST http://localhost:8001/chat -H "Content-Type: application/json" -d '{"prompt":"What is a LLM?"}'
