# Task 2: Image Layers

## Command
```bash
docker image history nginx
```

## Observations
When you run this command, you'll see output with multiple lines, each representing a layer in the image. You'll notice:
- Some layers display file sizes (e.g., 142MB, 5.2MB)
- Some layers show `0B` (these are metadata-only changes)

## Notes: What are layers and why does Docker use them?

### What are Layers?
Layers are read-only filesystem snapshots created during the Docker image build process. Each instruction in a Dockerfile (FROM, RUN, COPY, etc.) creates a new layer. These layers stack on top of each other to form the complete image.

### Why Docker Uses Layers?

1. **Efficiency** - Layers are cached. Unchanged layers don't need to be rebuilt, speeding up subsequent builds.

2. **Storage Optimization** - Docker uses copy-on-write. Multiple containers from the same image share identical base layers, reducing storage overhead.

3. **Reusability** - Layers can be reused across different images, avoiding duplication.

4. **Portability** - Layers enable incremental distribution—only changed layers need to be downloaded or uploaded.

5. **Debugging** - You can inspect individual layers to understand what each command added to the image.


## Task 3: Container Lifecycle

Practice the full lifecycle on one container:

1. **Create a container** (without starting it)
    ```bash
    docker create --name my-container nginx
    ```

2. **Start the container**
    ```bash
    docker start my-container
    ```

3. **Pause it and check status**
    ```bash
    docker pause my-containers
    docker ps -a
    ```

4. **Unpause it**
    ```bash
    docker unpause my-container
    ```

5. **Stop it**
    ```bash
    docker stop my-container
    ```

6. **Restart it**
    ```bash
    docker restart my-container
    ```
    ```

7. **Remove it**
    ```bash
    docker rm my-container
    ```

**Key Observation:** Check `docker ps -a` after each step to observe the state changes (created, running, paused, exited, removed).


## Task 4: Working with Running Containers

1. **Run an Nginx container in detached mode**
    ```bash
    docker run -d --name my-nginx -p 8080:80 nginx
    ```

2. **View its logs**
    ```bash
    docker logs my-nginx
    ```

3. **View real-time logs (follow mode)**
    ```bash
    docker logs -f my-nginx
    ```
    (Press `Ctrl+C` to exit)

4. **Exec into the container and look around the filesystem**
    ```bash
    docker exec -it my-nginx /bin/bash
    ls -la
    cat /etc/nginx/nginx.conf
    exit
    ```

5. **Run a single command inside the container without entering it**
    ```bash
    docker exec my-nginx nginx -v
    ```

6. **Inspect the container**
    ```bash
    docker inspect my-nginx
    ```
    Look for:
    - **IP Address**: `NetworkSettings.IPAddress`
    - **Port Mappings**: `NetworkSettings.Ports`
    - **Mounts**: `Mounts`

    Or use grep to find specific details:
    ```bash
    docker inspect my-nginx | grep -E "IPAddress|HostPort"
    ```

**Key Observation:** `docker logs` shows container output, `docker exec` lets you interact with running processes, and `docker inspect` reveals all configuration details about the container.


## Task 5: Cleanup

1. **Stop all running containers in one command**
    ```bash
    docker stop $(docker ps -q)
    ```

2. **Remove all stopped containers in one command**
    ```bash
    docker container prune -f
    ```

3. **Remove unused images**
    ```bash
    docker image prune -a -f
    ```

4. **Check how much disk space Docker is using**
    ```bash
    docker system df
    ```

**Key Observation:** Use `docker system df` to see a breakdown of image, container, and volume storage. Use `docker system prune` to remove all unused containers, images, and networks in one go.