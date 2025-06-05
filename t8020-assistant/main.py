from flask import Flask, request, jsonify

import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "c4816847c8774658901f10aca58da5e0")

@app.route('/getLocalNews', methods=['POST'])
def getLocalNews():
    data = request.get_json()
    required = ["location", "category", "limit"]
    missing = [key for key in required if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    location = data["location"]
    category = data["category"]
    limit = data["limit"]

    params = {
        "q": location,
        "category": category,
        "pageSize": limit,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get("https://newsapi.org/v2/top-headlines", params=params)
    if response.status_code != 200:
        return jsonify({"error": "News API error", "details": response.text}), 500

    news = response.json().get("articles", [])
    results = [
        {
            "title": item["title"],
            "summary": item.get("description", ""),
            "source": item["source"]["name"],
            "url": item["url"]
        }
        for item in news
    ]
    return jsonify(results)


@app.route('/getNationalNews', methods=['POST'])
def getNationalNews():
    data = request.get_json()
    required = ["category", "limit"]
    missing = [key for key in required if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    category = data["category"]
    limit = data["limit"]

    params = {
        "category": category,
        "country": "us",
        "pageSize": limit,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get("https://newsapi.org/v2/top-headlines", params=params)
    if response.status_code != 200:
        return jsonify({"error": "News API error", "details": response.text}), 500

    news = response.json().get("articles", [])
    results = [
        {
            "title": item["title"],
            "summary": item.get("description", ""),
            "source": item["source"]["name"],
            "url": item["url"]
        }
        for item in news
    ]
    return jsonify(results)


app = Flask(__name__)

@app.route('/getLocalNews', methods=['POST'])
def getLocalNews():
    data = request.get_json()
    missing = [key for key in ['location', 'category', 'limit'] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for getLocalNews
    return jsonify({"message": "Called getLocalNews successfully", "input": data})

@app.route('/getNationalNews', methods=['POST'])
def getNationalNews():
    data = request.get_json()
    missing = [key for key in ['category', 'limit'] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for getNationalNews
    return jsonify({"message": "Called getNationalNews successfully", "input": data})

@app.route('/getLocalSportsScores', methods=['POST'])
def getLocalSportsScores():
    data = request.get_json()
    missing = [key for key in ['team', 'sport', 'date'] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for getLocalSportsScores
    return jsonify({"message": "Called getLocalSportsScores successfully", "input": data})

@app.route('/getNationalSportsUpdates', methods=['POST'])
def getNationalSportsUpdates():
    data = request.get_json()
    missing = [key for key in ['league', 'date'] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for getNationalSportsUpdates
    return jsonify({"message": "Called getNationalSportsUpdates successfully", "input": data})

@app.route('/getTokenUsageInfo', methods=['POST'])
def getTokenUsageInfo():
    data = request.get_json()
    missing = [key for key in [] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for getTokenUsageInfo
    return jsonify({"message": "Called getTokenUsageInfo successfully", "input": data})

@app.route('/getCommunityEvents', methods=['POST'])
def getCommunityEvents():
    data = request.get_json()
    missing = [key for key in ['location', 'limit'] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for getCommunityEvents
    return jsonify({"message": "Called getCommunityEvents successfully", "input": data})

@app.route('/answerFAQ', methods=['POST'])
def answerFAQ():
    data = request.get_json()
    missing = [key for key in ['question'] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for answerFAQ
    return jsonify({"message": "Called answerFAQ successfully", "input": data})

@app.route('/sendProactiveSuggestions', methods=['POST'])
def sendProactiveSuggestions():
    data = request.get_json()
    missing = [key for key in ['userProfile'] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for sendProactiveSuggestions
    return jsonify({"message": "Called sendProactiveSuggestions successfully", "input": data})

@app.route('/handleUserGreeting', methods=['POST'])
def handleUserGreeting():
    data = request.get_json()
    missing = [key for key in [] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for handleUserGreeting
    return jsonify({"message": "Called handleUserGreeting successfully", "input": data})

@app.route('/verifyAndCiteSource', methods=['POST'])
def verifyAndCiteSource():
    data = request.get_json()
    missing = [key for key in ['content'] if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # TODO: Implement logic for verifyAndCiteSource
    return jsonify({"message": "Called verifyAndCiteSource successfully", "input": data})


if __name__ == '__main__':
    app.run(debug=True)


WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "demo")  # Replace 'demo' with your real API key
SPORTS_API_KEY = os.getenv("SPORTS_API_KEY", "demo")    # Replace 'demo' with your real API key

@app.route('/get_current_weather', methods=['POST'])
def get_current_weather():
    data = request.get_json()
    required = ["location", "format"]
    missing = [key for key in required if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    location = data["location"]
    unit = "m" if data["format"] == "celsius" else "f"
    params = {
        "q": location,
        "units": unit,
        "appid": WEATHER_API_KEY
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    if response.status_code != 200:
        return jsonify({"error": "Weather API error", "details": response.text}), 500

    weather = response.json()
    return jsonify({
        "location": weather["name"],
        "temperature": weather["main"]["temp"],
        "description": weather["weather"][0]["description"]
    })


@app.route('/getLocalSportsScores', methods=['POST'])
def getLocalSportsScores():
    data = request.get_json()
    required = ["team", "sport", "date"]
    missing = [key for key in required if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # Placeholder mock return (replace with a real sports API call if you have one)
    return jsonify({
        "team": data["team"],
        "opponent": "Rival Team",
        "score": "102-98",
        "highlights": "Team won in a close match!",
        "date": data["date"]
    })


@app.route('/getNationalSportsUpdates', methods=['POST'])
def getNationalSportsUpdates():
    data = request.get_json()
    required = ["league", "date"]
    missing = [key for key in required if key not in data]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400

    # Placeholder mock return (replace with a real sports API call if you have one)
    return jsonify([
        {
            "game": f"{data['league']} Match 1",
            "score": "110-107",
            "date": data["date"],
            "playerHighlights": "Player A scored 30 points"
        },
        {
            "game": f"{data['league']} Match 2",
            "score": "89-95",
            "date": data["date"],
            "playerHighlights": "Player B with a double-double"
        }
    ])
