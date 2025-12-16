FROM python:3.10-alpine
WORKDIR /app-backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000","--workers","2","app:app"]
