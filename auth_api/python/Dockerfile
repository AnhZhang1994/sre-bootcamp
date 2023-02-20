FROM python:3-alpine

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# Copy source code
COPY src/ .

# Expose port
EXPOSE 8000

# Start server
CMD ["python", "api.py"]
