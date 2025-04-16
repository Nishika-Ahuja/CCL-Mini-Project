from flask import Flask, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app, origins="*", supports_credentials=True) 


@app.route("/")
def home():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"""
    <h2>Order Service Running 📦</h2>
    <ul>
        <li><strong>Hostname:</strong> {hostname}</li>
        <li><strong>IP Address:</strong> {ip_address}</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
