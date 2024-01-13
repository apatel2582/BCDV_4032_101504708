# Author: Anishkumar Pankajkumar Patel
# Student ID: 101504708
# Date: 2024-01-13
# BCDV 4032: Lab 01

# Dockerfile for flask-app

# Base image
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip

# Install python dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy app files
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Expose port 5000
EXPOSE 5000

# Run app.py
CMD ["python", "/usr/src/app/app.py"]