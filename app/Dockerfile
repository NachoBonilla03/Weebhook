# Use a Python base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file and the Flask application to /app
COPY requirements.txt .
COPY app.py .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask-specific dependencies
RUN pip install flask

# Expose the port the Flask application will use
EXPOSE 8000

# Define the default command to run the application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
