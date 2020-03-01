# Using official python runtime base image
#FROM python:3.5-alpine
FROM python:3.7-buster

# Set the application directory
WORKDIR /flask-app

# Install our requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# Copy our code from the current folder to /app inside the container

COPY . .


# Define our command to be run when launching the container
#CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]

