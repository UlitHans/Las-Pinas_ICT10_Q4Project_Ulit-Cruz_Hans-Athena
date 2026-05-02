from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path

app = Flask(__name__, static_folder='.', template_folder='.')

classmates = [
    {"name": "Kristine", "section": "Amethyst", "subject": "Math"},
    {"name": "Jean", "section": "Amethyst", "subject": "Science"},
    {"name": "Hariette", "section": "Amethyst", "subject": "English"},
    {"name": "Jubilee", "section": "Amethyst", "subject": "Math"},
    {"name": "Vivian", "section": "Amethyst", "subject": "History"},
    {"name": "Luisito", "section": "Topaz", "subject": "Math"},
    {"name": "Renn", "section": "Topaz", "subject": "Math"},
    {"name": "Josua", "section": "Topaz", "subject": "Math"}
]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/classmates', methods=['GET'])
def get_classmates():
    return jsonify(classmates)

@app.route('/api/classmates', methods=['POST'])
def add_classmate():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON payload."}), 400

    name = str(data.get('name', '')).strip()
    section = str(data.get('section', '')).strip()
    subject = str(data.get('subject', '')).strip()

    if not name or not section or not subject:
        return jsonify({"error": "Name, section, and subject are required."}), 400

    new_classmate = {"name": name, "section": section, "subject": subject}
    classmates.append(new_classmate)
    return jsonify(new_classmate), 201

@app.route('/<path:path>')
def static_proxy(path):
    target = Path(path)
    if target.exists():
        return send_from_directory('.', path)
    return jsonify({"error": "Not found."}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)