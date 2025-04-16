from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows requests from frontend like GitHub Pages

API_KEY = "b2e818a492563b45e312fccc396702d8da3429740b970deb4639b4e6aba26d1022c906234a66f4ac"
@app.route("/check-ip", methods=["GET"])
def check_ip():
    ip = request.args.get("ip")
    if not ip:
        return jsonify({"error": "No IP provided"}), 400

    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(url, headers=headers, params=params)
    return jsonify(response.json())
