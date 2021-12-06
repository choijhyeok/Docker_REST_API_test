#!/bin/sh
export FLASK_APP=./server_api.py
flask run -h 0.0.0.0 -p 50022
