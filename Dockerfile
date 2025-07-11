# Use a slim Python base image
FROM python:3.10-slim

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set up the google-search-mcp
RUN cd google-search-mcp && \
    npm install && \
    npm run build && \
    chmod 755 dist/index.js

# Ensure frontend directory exists and has proper permissions
RUN mkdir -p frontend && chmod 755 frontend

# Command to run the FastAPI application
CMD ["python", "main.py"]