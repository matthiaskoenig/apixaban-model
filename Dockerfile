# Dockerfile for apixaban
# -----------------------
# Build and push image
#   docker build -f Dockerfile -t matthiaskoenig/apixaban:0.5.1 -t matthiaskoenig/apixaban:latest .
#   docker login
#   docker push --all-tags matthiaskoenig/apixaban
FROM python:3.14-slim

# install uv
COPY --from=ghcr.io/astral-sh/uv:0.10.8 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

# install git
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

# copy code
WORKDIR /code
COPY .python-version /code/python-version.py
COPY pyproject.toml /code/pyproject.toml
COPY README.md /code/README.md
COPY src /code/src
COPY uv.lock /code/uv.lock

# install package
RUN uv pip install -e .
