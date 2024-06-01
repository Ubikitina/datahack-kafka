# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt into the working directory
COPY requirements.txt ./

# Install project dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all Python files from the current directory on the host to the working directory in the container
COPY *.py .

# Define the command to run the application
CMD [ "python", "./app.py" ]