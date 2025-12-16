from flask import Flask, jsonify,request
from datetime import datetime
import socket
import time

app = Flask(__name__)

start_time = time.time()

@app.route('/')
def index():
    return jsonify({
        'message' : 'Hello from backend',
        'timestamp' : datetime.now().isoformat(),
        'hostname' : socket.gethostname(),
        'headers' : {
            'host': request.headers.get("Host")
        }
    })


@app.route('/api/users')
def users():
    return jsonify({
        'users' : [
            {"id" : 1, "name":"Jan Kowalski" },
            {"id" : 2, "name":"Anna Nowacka" },
            {"id" : 3, "name":"Piotr Wiśniewski" },
        ]
    })

@app.route('/health')
def health():
    uptime = time.time() - start_time
    return jsonify({
        'status': 'health',
        'uptime' : uptime
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)# __name__