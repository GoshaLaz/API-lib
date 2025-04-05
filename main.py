# Імпорт бібліотек для роботи з API
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
server_url = "http://localhost:5001"  # URL C++ сервера

# В app.route() вказуємо де і які API-методи використовуються

# Користувачі
# Реєструємо нового користувача
@app.route("/register", methods=["POST"])
def register():
    response = requests.post(f"{server_url}/register", json=request.json) # Надсилаємо HTTP POST-запит з реєстрацією користувача
    return jsonify(response.json()), response.status_code # Повертаємо HTTP POST-запит

# Відсилаємо логін користувача 
@app.route("/login", methods=["POST"])
def login():
    response = requests.post(f"{server_url}/login", json=request.json) # Надсилаємо HTTP POST-запит з логіном користувача
    return jsonify(response.json()), response.status_code # Повертаємо HTTP POST-запит

# Перевіряємо та редагуємо профіль користувача 
@app.route("/users/<int:user_id>", methods=["GET", "PUT"])
def user_profile(user_id):
    if request.method == "GET": 
        response = requests.get(f"{server_url}/users/{user_id}")  # Надсилаємо HTTP GET-запит з даними користувача
    else:
        response = requests.put(f"{server_url}/users/{user_id}", json=request.json) # Надсилаємо HTTP PUT-запит з оновленням даних користувача
    return jsonify(response.json()), response.status_code # Повертаємо HTTP GET-запит або HTTP PUT-запит

# Події
# Основи подій 
@app.route("/events", methods=["GET", "POST"])
def events():
    if request.method == "GET":
        response = requests.get(f"{server_url}/events", params=request.args) # Надсилаємо HTTP GET-запит з даними події
    else:
        response = requests.post(f"{server_url}/events", json=request.json) # Надсилаємо HTTP POST-запит з даними події
    return jsonify(response.json()), response.status_code # Повертаємо HTTP GET-запит або HTTP POST-запит

# Деталі подій 
@app.route("/events/<int:event_id>", methods=["GET", "PUT", "DELETE"])
def event_detail(event_id):
    if request.method == "GET":
        response = requests.get(f"{server_url}/events/{event_id}") # Надсилаємо HTTP GET-запит з детальними даними події
    elif request.method == "PUT":
        response = requests.put(f"{server_url}/events/{event_id}", json=request.json) # Надсилаємо HTTP PUT-запит з детальними даними події
    else:
        response = requests.delete(f"{server_url}/events/{event_id}") # Надсилаємо HTTP DELETE-запит з видаленням детальними даними події
    return jsonify(response.json()), response.status_code # Повертаємо HTTP GET-запит, HTTP PUT-запит або HTTP DELETE-запит

# Завдання
# Основи завдань
@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "GET":
        response = requests.get(f"{server_url}/tasks", params=request.args) # Надсилаємо HTTP GET-запит з даними завдання 
    else:
        response = requests.post(f"{server_url}/tasks", json=request.json) # Надсилаємо HTTP POST-запит з даними завдання
    return jsonify(response.json()), response.status_code # Повертаємо HTTP GET-запит або HTTP POST-запит

@app.route("/tasks/<int:task_id>", methods=["GET", "PUT", "DELETE"])
def task_detail(task_id):
    if request.method == "GET":
        response = requests.get(f"{server_url}/tasks/{task_id}") # Надсилаємо HTTP GET-запит з детальними даними завдання
    elif request.method == "PUT":
        response = requests.put(f"{server_url}/tasks/{task_id}", json=request.json) # Надсилаємо HTTP PUT-запит з детальними даними завдання
    else:
        response = requests.delete(f"{server_url}/tasks/{task_id}") # Надсилаємо HTTP DELETE-запит з видаленням детальними даними завдання
    return jsonify(response.json()), response.status_code # Повертаємо HTTP GET-запит, HTTP PUT-запит або HTTP DELETE-запит

if __name__ == "__main__":
    app.run(debug=True) # Запускаємо бібліотеку
