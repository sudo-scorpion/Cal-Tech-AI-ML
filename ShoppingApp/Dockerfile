# Use an official Python runtime as a parent image
FROM python:3.9-slim as backend

# Set the working directory for the Flask application
WORKDIR /usr/src/app/backend

# Copy the Flask dependencies file to the working directory
COPY shopping-app-server/requirements.txt ./

# # Install Python, pip, and Gunicorn for serving the Flask app
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install gunicorn && \
    rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Flask application code to the working directory
COPY shopping-app-server/ .

# Stage 1: Build the Angular application
FROM node:20 as frontend
WORKDIR /app
COPY shopping-app-ui/package.json shopping-app-ui/package-lock.json ./
RUN npm install
COPY shopping-app-ui/ .
RUN npm run build

# Stage 2: Setup Nginx to serve both Angular and Flask
FROM nginx:alpine

# Copy Angular static files
COPY --from=frontend /app/dist/shopping-app-ui/browser/ /usr/share/nginx/html

# Copy Flask application from the backend stage
COPY --from=backend /usr/src/app/backend /backend

# Nginx configuration for serving Angular and proxying API requests
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

# Expose ports for both the Angular app (80) and the Flask API (5000)
EXPOSE 80 5000

# # Define environment variables
# ENV FLASK_APP=run.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_ENV=development

# Start Nginx and Gunicorn for Flask
CMD nginx -g 'daemon off;' && gunicorn -w 4 -b 0.0.0.0:5000 -chdir /backend run:app
# CMD gunicorn -w 4 -b /backend/run:app && nginx -g 'daemon off;'

# The Dockerfile is divided into three stages: 
# The first stage installs the Python runtime and dependencies for the Flask application. The second stage builds the Angular application. The third stage sets up Nginx to serve both the Angular and Flask applications. 
# The  nginx.conf  and  default.conf  files are used to configure Nginx to serve the Angular application and proxy API requests to the Flask application. 
# The  nginx.conf  file is used to configure Nginx to serve the Angular application. 
# Path: ShoppingApp/nginx.conf
