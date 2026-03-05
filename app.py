from flask import Flask, jsonify

app = Flask(__name__)

# Health check — CI/CD pipelines often ping this to verify the app is alive
@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "1.0.0"})

@app.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)