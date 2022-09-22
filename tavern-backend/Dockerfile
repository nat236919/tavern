FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

# Setup Working Directory
WORKDIR /app

# Install dependencies
COPY Pipfile Pipfile.lock requirements.txt .
RUN pip install pipenv && \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
    pipenv install --deploy --system && \
    apt-get remove -y gcc python3-dev libssl-dev && \
    apt-get autoremove -y && \
    pip uninstall pipenv -y

# Copy all files to the current working directory
COPY app/ .