# llama-cpp-fastapi-service
Use Fastapi to serve the llama 2 cpp fastapi service.

# FastAPI Docker Container

This repository provides an optimized Docker container setup for running a FastAPI application.

## Features

- Utilizes the official Python 3.9 slim image as the base.
- Optimized installation of system packages to reduce container size.
- Pip-based Python dependency management with optimizations to minimize caching and speed up installs.

## Usage

### I. Directly via Docker

1. Clone this repository:
```bash
git clone https://github.com/LiuYuWei/llama-cpp-fastapi-service.git
cd llama-cpp-fastapi-service
```

2. Build your Docker image:
```bash
docker build -t fastapi-container .
```

3. Run your FastAPI application:
```bash
# Your FastAPI application should now be running at http://localhost:8000.
docker run -p 8000:8000 fastapi-container
```

### II. Using Make Commands

1. Clone this repository:
```bash
git clone https://github.com/LiuYuWei/llama-cpp-fastapi-service.git
cd llama-cpp-fastapi-service
```

2. To build the Docker image:
```bash
make build
```

3. To push the Docker image:
```bash
make push
```

4. To run the FastAPI application:
```bash
# Your FastAPI application should now be running at http://localhost:8000.
make run
```

5. To view the logs:
```bash
make logs
```

6. To remove the running container:
```bash
make remove
```

## Contributing

If you have suggestions or changes, please submit a pull request or open an issue.