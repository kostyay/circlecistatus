# ---- Base python ----
FROM python:3.6-alpine AS base
# Create app directory
WORKDIR /app

# ---- Dependencies ----
FROM base AS dependencies
COPY requirements.txt ./
RUN apk add --no-cache libgcc git build-base libffi-dev libgit2 libgit2-dev && \
    pip install -r requirements.txt

# ---- Copy Files/Build ----
FROM dependencies AS build
WORKDIR /app
COPY . /app
COPY --from=dependencies /root/.cache /root/.cache
WORKDIR /app

ENTRYPOINT [ "python", "./build_status.py" ]

