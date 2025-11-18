FROM python:3.11

WORKDIR /app

# kopiowanie pliku
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY app.py .




EXPOSE 5000
CMD ["python", "app.py"]