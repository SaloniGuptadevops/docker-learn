# Docker

## Overview
Docker is a containerization platform that packages applications and dependencies into isolated, portable containers.

## Key Concepts
- **Image**: A blueprint for creating containers
- **Container**: A running instance of an image
- **Registry**: A repository for storing and sharing images (e.g., Docker Hub)
- **Dockerfile**: A script that defines image build steps

## Basic Commands
```bash
docker build -t image-name .           # Build an image
docker run -d --name container image   # Run a container
docker ps                              # List running containers
docker logs container-name             # View container logs
docker stop container-name             # Stop a container
docker push image-name                 # Push to registry
```

## Benefits
- Consistency across environments
- Lightweight and fast deployment
- Simplified dependency management
- Scalability and orchestration support
