# Use the official Python image from the Docker Hub
FROM python:3.11

# Set environment variables
ENV POETRY_VERSION=1.8.2

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

ADD sayvai_sqlagent /app/sayvai_sqlagent
# Install the dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the application code into the container
# COPY . .

# Specify the command to run the FastAPI application using Poetry
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
