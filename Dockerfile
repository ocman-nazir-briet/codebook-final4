# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose port 8000 to the host machine
EXPOSE 8000

# Define the command to run the application when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
