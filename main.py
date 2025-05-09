# Імпорт бібліотек для роботи з API
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
server_url = "http://localhost:5000"  # URL C++ сервера

# Список для зберігання подій
events_storage = []
event_id_counter = 1

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
    global event_id_counter

    if request.method == "GET":
        return jsonify(events_storage), 200
    else:
        data = request.json
        data["id"] = event_id_counter
        event_id_counter += 1
        events_storage.append(data)
        return jsonify({"message": "Подія створена", "event": data}), 201

@app.route("/events/<int:event_id>", methods=["GET", "PUT", "DELETE"])
def event_detail(event_id):
    global events_storage
    event = next((e for e in events_storage if e["id"] == event_id), None)

    if not event:
        return jsonify({"error": "Подію не знайдено"}), 404

    if request.method == "GET":
        return jsonify(event), 200
    elif request.method == "PUT":
        event.update(request.json)
        return jsonify({"message": "Подію оновлено", "event": event}), 200
    elif request.method == "DELETE":
        events_storage = [e for e in events_storage if e["id"] != event_id]
        return jsonify({"message": "Подію видалено"}), 200

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
    app.run(debug=True, port=5000)
