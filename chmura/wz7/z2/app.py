# hostowana na porcie 8080 /9123
# dzialalała na roocie /        napisać funkcje hello() - która zwraca "Hello, World!"
from flask import Flask     
import os
PORT = int(os.getenv("PORT", 9123))

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)