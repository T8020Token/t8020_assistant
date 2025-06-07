import streamlit as st
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Load API keys from Streamlit secrets
NEWS_API_KEY = st.secrets.get("NEWS_API_KEY")
WEATHER_API_KEY = st.secrets.get("WEATHER_API_KEY")
ZILLOW_API_KEY = st.secrets.get("ZILLOW_API_KEY")
SPORTS_API_KEY = st.secrets.get("SPORTS_API_KEY")
GNEWS_API_KEY = st.secrets.get("GNEWS_API_KEY")

# ✅ Root route to confirm backend is live
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "✅ T8020 Flask backend is running"})

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
    return jsonify({
        "location": location,
        "listings": [
            {"price": "$450,000", "address": "123 Elm St", "bedrooms": 3, "bathrooms": 2},
            {"price": "$675,000", "address": "456 Oak Ave", "bedrooms": 4, "bathrooms": 3}
        ]
    })

@app.route("/getGNewsWorld", methods=["POST"])
def get_gnews_world():
    data = request.json
    keyword = data.get("keyword", "world")
    limit = data.get("limit", 5)
    url = f"https://gnews.io/api/v4/search?q={keyword}&lang=en&country=us&max={limit}&token={GNEWS_API_KEY}"
    return jsonify(requests.get(url).json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
