from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask app running in Docker"})

@app.route('/hello/<name>')
def hello(name):
    return jsonify({"message": f"Hello, {name}! This is Flask in Docker 🚀"})

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    return jsonify({"result": a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
