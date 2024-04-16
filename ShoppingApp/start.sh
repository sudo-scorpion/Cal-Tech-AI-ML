#!/bin/sh
# Start Nginx in the background
nginx &
# Start Gunicorn
gunicorn -w 4 -b 127.0.0.1:5000 shopping-app-server:run
