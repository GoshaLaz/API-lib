from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
server_url = "http://localhost:5001"  # URL C++ сервера

# Користувачі
@app.route("/register", methods=["POST"])
def register():
    response = requests.post(f"{server_url}/register", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route("/login", methods=["POST"])
def login():
    response = requests.post(f"{server_url}/login", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route("/users/<int:user_id>", methods=["GET", "PUT"])
def user_profile(user_id):
    if request.method == "GET":
        response = requests.get(f"{server_url}/users/{user_id}")
    else:
        response = requests.put(f"{server_url}/users/{user_id}", json=request.json)
    return jsonify(response.json()), response.status_code

# Події
@app.route("/events", methods=["GET", "POST"])
def events():
    if request.method == "GET":
        response = requests.get(f"{server_url}/events", params=request.args)
    else:
        response = requests.post(f"{server_url}/events", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route("/events/<int:event_id>", methods=["GET", "PUT", "DELETE"])
def event_detail(event_id):
    if request.method == "GET":
        response = requests.get(f"{server_url}/events/{event_id}")
    elif request.method == "PUT":
        response = requests.put(f"{server_url}/events/{event_id}", json=request.json)
    else:
        response = requests.delete(f"{server_url}/events/{event_id}")
    return jsonify(response.json()), response.status_code

# Завдання
@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "GET":
        response = requests.get(f"{server_url}/tasks", params=request.args)
    else:
        response = requests.post(f"{server_url}/tasks", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route("/tasks/<int:task_id>", methods=["GET", "PUT", "DELETE"])
def task_detail(task_id):
    if request.method == "GET":
        response = requests.get(f"{server_url}/tasks/{task_id}")
    elif request.method == "PUT":
        response = requests.put(f"{server_url}/tasks/{task_id}", json=request.json)
    else:
        response = requests.delete(f"{server_url}/tasks/{task_id}")
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
