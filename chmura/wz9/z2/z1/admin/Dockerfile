FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 4000
CMD ["gunicorn", "--bind", "0.0.0.0:4000","--workers","2","app:app"]
