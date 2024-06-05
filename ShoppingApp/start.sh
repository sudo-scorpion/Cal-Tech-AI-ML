#!/bin/sh
# Start Nginx in the background
nginx -g 'daemon off;' &

# Start Gunicorn to serve the Flask application
cd /backend
gunicorn -w 4 -b localhost:5000 run:app
