# Use Debian or Alpine as the base image
FROM debian:latest

# Install necessary packages for the Python script
RUN apt-get update && apt-get install -y python3 python3-pip


# Set the working directory inside the container
WORKDIR /home

# Install Python packages needed for the script
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r /home/requirements.txt

# Copy the Python script into the container
COPY logger.py .


# Define a named Docker volume
VOLUME /project_volume1

# Run the Python script and create a file inside the Docker volume
CMD python3 logger.py
