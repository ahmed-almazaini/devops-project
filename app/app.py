from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/")
def home():
    return f"""
    <h1>DevOps Team Service</h1>
    <p>Version: {VERSION}</p>
    <p>Status: Running</p>
    """

@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        version=VERSION
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
