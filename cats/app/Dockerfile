# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY cats/app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY cats/app/ /app/

# Expose port (e.g., 5000)
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]