from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask DevOps API running"

@app.route("/health")
def health():
    return jsonify({"status": "running", "service": "flask-devops-api"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)