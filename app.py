
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

# Task model (for simplicity, just using a dictionary)
# Each task will have an 'id', 'title', and 'done' status

# Create a new task (POST)
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()  # Get the JSON data from the request body
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400

    task = {
        'id': len(tasks) + 1,  # Simple auto-increment ID
        'title': data['title'],
        'done': False
    }
    tasks.append(task)
    return jsonify(task), 201

# Get all tasks (GET)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Get a specific task by ID (GET)
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

# Update a task (PUT)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if 'title' in data:
        task['title'] = data['title']
    if 'done' in data:
        task['done'] = data['done']
    
    return jsonify(task)

# Edit a task (PATCH)
@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def edit_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if 'title' in data:
        task['title'] = data['title']
    if 'done' in data:
        task['done'] = data['done']
    
    return jsonify(task)

# Delete a task (DELETE)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
