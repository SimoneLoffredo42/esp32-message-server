from flask import Flask, request

app = Flask(__name__)
latest_message = ""

@app.route('/send', methods=['POST'])
def send_message():
    global latest_message
    latest_message = request.form.get('message', '')
    return f"Messaggio ricevuto: {latest_message}"

@app.route('/get', methods=['GET'])
def get_message():
    return latest_message

app.run()

