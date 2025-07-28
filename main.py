from flask import Flask, request, jsonify
import os

app = Flask(__name__)
last_message = ""

@app.route("/message", methods=["POST"])
def set_message():
    global last_message
    data = request.get_json()
    last_message = data.get("message", "")
    return jsonify({"status": "received", "message": last_message})

@app.route("/message", methods=["GET"])
def get_message():
    global last_message
    return jsonify({"message": last_message})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
