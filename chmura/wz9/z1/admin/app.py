from flask import Flask, jsonify,request
from datetime import datetime
import socket
import time

app = Flask(__name__)

start_time = time.time()

@app.route('/')
def index():
    return jsonify({
        'message' : 'Hello from admin',
        'timestamp' : datetime.now().isoformat(),
        'hostname' : socket.gethostname(),
        'headers' : {
            'host': request.headers.get("Host")
        }
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)# __name__