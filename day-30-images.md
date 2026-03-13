
# Day 30: Docker Images

## Task 1: Docker Images

### Pull Images from Docker Hub

First, I pulled the nginx, ubuntu, and alpine images:

```bash
docker pull nginx
docker pull ubuntu
docker pull alpine
```

### List All Images and Compare Sizes

```bash
docker images
```

**Output:**
```
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
nginx         latest    ed21b7a8aee9   2 weeks ago    187MB
ubuntu        latest    3b418d874dee   5 days ago     77.8MB
alpine        latest    7e01a0d0a1dc   3 weeks ago    7.05MB
```

### Compare Ubuntu vs Alpine

Alpine is significantly smaller (7.05MB) compared to Ubuntu (77.8MB). This is because:

- **Alpine** uses musl libc instead of glibc, removing unnecessary system packages
- **Ubuntu** includes a full package management system and many base utilities
- Alpine is minimal by design, ideal for containers where size matters

### Inspect an Image

```bash
docker inspect ubuntu:latest
```

From the output, I can see:
- Image ID and digest
- Creation date
- Architecture and OS
- Exposed ports and environment variables
- Entry point and default command
- Layers and their sizes

### Remove an Image

```bash
docker rmi nginx:latest
```

This removes the nginx image from my machine.
