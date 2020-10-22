#!/bin/bash
export FLASK_APP=app.py
export SERVICE_ADDRESS=http://127.0.0.1:5001
flask run -p 5000
