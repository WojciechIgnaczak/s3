# uruchamia app w python
# działa na obrazie python:3.9-slim
# działał na katalogu app
# kopiowanie wymaganych plików
#instalacja zależności
# widoczny na porcie 8080

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 9123
CMD ["python", "app.py"]