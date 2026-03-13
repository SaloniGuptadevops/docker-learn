# Day 31: Dockerfile Tasks

## Task 1: Your First Dockerfile

1. Create a folder: `my-first-image`
2. Inside, create a `Dockerfile`:

```dockerfile
FROM ubuntu
RUN apt-get update && apt-get install -y curl
CMD echo "Hello from my custom image!"
```

3. Build the image:

```bash
docker build -t my-ubuntu:v1 .
```

4. Run the container:

```bash
docker run my-ubuntu:v1
```

**Verify:** The message prints.

---

## Task 2: Dockerfile Instructions

Example Dockerfile:

```dockerfile
FROM ubuntu
RUN apt-get update && apt-get install -y curl
COPY hello.txt /app/hello.txt
WORKDIR /app
EXPOSE 8080
CMD ["cat", "hello.txt"]
```

- `FROM`: Sets base image.
- `RUN`: Executes commands during build.
- `COPY`: Copies files from host.
- `WORKDIR`: Sets working directory.
- `EXPOSE`: Documents port.
- `CMD`: Default command.

Build and run:

```bash
docker build -t instruction-demo .
docker run instruction-demo
```

---

## Task 3: CMD vs ENTRYPOINT

**CMD Example:**

```dockerfile
FROM ubuntu
CMD ["echo", "hello"]
```

- Run: `docker run cmd-demo`
- Custom command: `docker run cmd-demo echo world` (overrides CMD)

**ENTRYPOINT Example:**

```dockerfile
FROM ubuntu
ENTRYPOINT ["echo"]
```

- Run: `docker run entrypoint-demo` (prints nothing)
- With args: `docker run entrypoint-demo world` (prints "world")

**Notes:**  
- Use CMD for default commands that can be overridden.
- Use ENTRYPOINT for fixed commands, passing arguments.

---

## Task 4: Build a Simple Web App Image

1. Create `index.html` with content.
2. Dockerfile:

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
```

3. Build:

```bash
docker build -t my-website:v1 .
```

4. Run:

```bash
docker run -p 8080:80 my-website:v1
```

Access in browser: `http://localhost:8080`

---

## Task 5: .dockerignore

Create `.dockerignore`:

```
node_modules
.git
*.md
.env
```

Build image and verify ignored files are not included.

---

## Task 6: Build Optimization

- Docker caches layers.
- Changing a line invalidates cache for subsequent layers.
- Place frequently changing lines last for faster builds.

**Notes:**  
Layer order matters for build speed because Docker only rebuilds layers after a change.