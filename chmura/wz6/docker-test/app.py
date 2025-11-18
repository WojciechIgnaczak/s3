from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)
#Konfiguracja env zmiennych
PORT = int(os.getenv("PORT", 5000))
VERSION = os.getenv("VERSION", "1.0.0")

# in memory storage for demonstration purposes
tasks = []

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "version": VERSION, "timestamp": datetime.now().isoformat()})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    task={
        'id': len(tasks) + 1,
        'title': request.json.get('title'),
        'done': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(task)
    return jsonify(task), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task=next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['done']= request.json.get('done', task['done'])
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404


if __name__ == '__main__':
    print(f"Starting app on port {PORT} with version {VERSION}")
    app.run(host='0.0.0.0', port=PORT)