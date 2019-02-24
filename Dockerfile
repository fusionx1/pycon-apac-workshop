# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory /app
WORKDIR /app

#Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

ENV pop World

CMD ["python", "/app/app/app.py"]

