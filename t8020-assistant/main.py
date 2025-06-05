
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_current_weather", methods=["POST"])
def get_current_weather():
    data = request.json
    return jsonify({
        "location": data["location"],
        "format": data["format"],
        "temperature": "24",
        "unit": "C" if data["format"] == "celsius" else "F"
    })

@app.route("/getLocalNews", methods=["POST"])
def get_local_news():
    data = request.json
    return jsonify({
        "location": data["location"],
        "category": data["category"],
        "articles": [{"title": "Sample News", "url": "https://example.com"}] * data.get("limit", 5)
    })

@app.route("/getCommunityEvents", methods=["POST"])
def get_community_events():
    data = request.json
    return jsonify({
        "location": data["location"],
        "events": [{"title": "Sample Event", "date": "2025-06-01"}] * data.get("limit", 5)
    })

if __name__ == "__main__":
    app.run(port=5000)
