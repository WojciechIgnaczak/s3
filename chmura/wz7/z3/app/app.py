# hostowana na porcie 8080 /9123
# dzialalała na roocie /        napisać funkcje hello() - która zwraca "Hello, World!"
from flask import Flask 
from redis import Redis, RedisError    
import os
#PORT = int(os.getenv("PORT", 8080))

app = Flask(__name__)
redis= Redis(host="redis", port=6379, db=0, decode_responses=True)

@app.route("/")
def index():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>brak polaczenia z redisem</i>"
    
    return f"Liczba odwiedzin: {visits}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)