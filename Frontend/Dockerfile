# Stage 1: Build Stage
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/


# Stage 2: Runtime Stage
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the installed Python packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/streamlit /usr/local/bin/

# Copy the rest of the application code from the builder stage
COPY --from=builder /app /app

# Expose the port that Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app2.py", "--server.port=8501", "--server.address=0.0.0.0"]