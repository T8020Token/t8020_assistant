from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
ZILLOW_API_KEY = os.environ.get("ZILLOW_API_KEY")
SPORTS_API_KEY = os.environ.get("SPORTS_API_KEY")

@app.route("/getLocalNews", methods=["POST"])
def get_local_news():
    data = request.json
    category = data.get("category")
    limit = data.get("limit", 5)
    url = f"https://newsapi.org/v2/top-headlines?q={category}&pageSize={limit}&apiKey={NEWS_API_KEY}"
    return jsonify(requests.get(url).json())

@app.route("/getNationalNews", methods=["POST"])
def get_national_news():
    data = request.json
    category = data.get("category")
    limit = data.get("limit", 5)
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&pageSize={limit}&apiKey={NEWS_API_KEY}"
    return jsonify(requests.get(url).json())

@app.route("/getWorldNews", methods=["POST"])
def get_world_news():
    data = request.json
    category = data.get("category")
    limit = data.get("limit", 5)
    url = f"https://newsapi.org/v2/top-headlines?language=en&category={category}&pageSize={limit}&apiKey={NEWS_API_KEY}"
    return jsonify(requests.get(url).json())

@app.route("/get_current_weather", methods=["POST"])
def get_current_weather():
    data = request.json
    location = data.get("location")
    units = "metric" if data.get("format") == "celsius" else "imperial"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units={units}"
    return jsonify(requests.get(url).json())

@app.route("/getLocalSportsScores", methods=["POST"])
def get_local_sports_scores():
    data = request.json
    return jsonify({
        "team": data.get("team"),
        "sport": data.get("sport"),
        "date": data.get("date"),
        "score": "92-87",
        "opponent": "City Rivals",
        "highlights": "Team won in the final seconds."
    })

@app.route("/getNationalSportsUpdates", methods=["POST"])
def get_national_sports_updates():
    data = request.json
    return jsonify({
        "league": data.get("league"),
        "date": data.get("date"),
        "games": [
            {"game": "Lakers vs Celtics", "score": "102-99", "date": data.get("date"), "playerHighlights": "LeBron scored 38."}
        ]
    })

@app.route("/getZillowListings", methods=["POST"])
def get_zillow_listings():
    data = request.json
    location = data.get("location")
    # Replace this with real Zillow API call if available
    return jsonify({
        "location": location,
        "listings": [
            {"price": "$450,000", "address": "123 Elm St", "bedrooms": 3, "bathrooms": 2},
            {"price": "$675,000", "address": "456 Oak Ave", "bedrooms": 4, "bathrooms": 3}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/getGNewsWorld", methods=["POST"])
def get_gnews_world():
    data = request.json
    keyword = data.get("keyword", "world")
    limit = data.get("limit", 5)
    gnews_api_key = os.environ.get("GNEWS_API_KEY")
    url = f"https://gnews.io/api/v4/search?q={keyword}&lang=en&country=us&max={limit}&token={gnews_api_key}"
    return jsonify(requests.get(url).json())