from flask import Flask, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


@app.route("/")
def index():
    return jsonify({"message": "Hello, DevSecOps!", "status": "ok"})


@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify({"result": add(a, b)})


@app.route("/subtract/<int:a>/<int:b>")
def subtract_route(a, b):
    return jsonify({"result": subtract(a, b)})


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
