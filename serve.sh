#!/bin/bash

source venv/bin/activate && flask --app server.py --debug run --host=0.0.0.0 --port=5001 
