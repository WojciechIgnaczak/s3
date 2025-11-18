FROM python:3.11-slim
ARG APP_VERSION=1.0.0
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
LABEL description="Aplikacja ${APP_VERSION}"

