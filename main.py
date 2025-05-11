from flask import Flask, request, jsonify

app = Flask(__name__)

# Зберігання подій і завдань
events = []
tasks = []
event_id_counter = 1
task_id_counter = 1

# ===================== ПОДІЇ =====================
@app.route("/events", methods=["GET", "POST"])
def handle_events():
    global event_id_counter

    if request.method == "GET":
        return jsonify(events), 200

    data = request.json
    required_fields = ["title", "date", "type", "description"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Не вказано поле: {field}"}), 400

    data["id"] = event_id_counter
    event_id_counter += 1
    events.append(data)
    return jsonify({"message": "Подію створено", "event": data}), 201


@app.route("/events/<int:event_id>", methods=["GET", "PUT", "DELETE"])
def handle_event(event_id):
    global events
    event = next((e for e in events if e["id"] == event_id), None)

    if not event:
        return jsonify({"error": "Подію не знайдено"}), 404

    if request.method == "GET":
        return jsonify(event), 200

    if request.method == "PUT":
        for key in ["title", "date", "type", "description"]:
            if key in request.json:
                event[key] = request.json[key]
        return jsonify({"message": "Подію оновлено", "event": event}), 200

    if request.method == "DELETE":
        events = [e for e in events if e["id"] != event_id]
        return jsonify({"message": "Подію видалено"}), 200

# ===================== ЗАВДАННЯ =====================
@app.route("/tasks", methods=["GET", "POST"])
def handle_tasks():
    global task_id_counter

    if request.method == "GET":
        return jsonify(tasks), 200

    data = request.json
    required_fields = ["title", "due_date", "content"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Не вказано поле: {field}"}), 400

    data["id"] = task_id_counter
    task_id_counter += 1
    tasks.append(data)
    return jsonify({"message": "Завдання створено", "task": data}), 201


@app.route("/tasks/<int:task_id>", methods=["GET", "PUT", "DELETE"])
def handle_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Завдання не знайдено"}), 404

    if request.method == "GET":
        return jsonify(task), 200

    if request.method == "PUT":
        for key in ["title", "due_date", "content"]:
            if key in request.json:
                task[key] = request.json[key]
        return jsonify({"message": "Завдання оновлено", "task": task}), 200

    if request.method == "DELETE":
        tasks = [t for t in tasks if t["id"] != task_id]
        return jsonify({"message": "Завдання видалено"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
