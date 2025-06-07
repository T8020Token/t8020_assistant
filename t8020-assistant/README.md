
# 🤖 T8020 Assistant

T8020 Assistant is an intelligent, fine-tuned chatbot powered by GPT-4 and real-time data APIs. It helps users stay up to date with:

- 🌍 World and national news
- 🏘️ Real estate listings (via Zillow)
- 🏈 Live sports scores and schedules
- ☀️ Local weather
- 📅 Community events
- ❓ FAQs and platform suggestions

## 🧰 Features

| Function                | Purpose                                            | API Source               |
|------------------------|----------------------------------------------------|--------------------------|
| `get_current_weather`  | Live weather by city & unit                        | WeatherAPI               |
| `getLocalNews`         | Local news by city, category, and limit           | NewsAPI.org              |
| `getNationalNews`      | National U.S. news by category                     | NewsAPI.org              |
| `getWorldNews`         | Global headlines and updates                       | GNews.io                 |
| `getZillowListings`    | Real estate listings by city and zip              | Zillow (via RapidAPI)    |
| `getCommunityEvents`   | Community events (custom or local data)           | Manual / Future          |
| `getNationalSportsUpdates` | Sports scores and highlights               | SportScoreAPI / RapidAPI |
| `answerFAQ`, `verifyAndCiteSource`, `sendProactiveSuggestions`, etc. | GPT-4 Tools | OpenAI Fine-tuning      |

## 📦 Project Structure

```
t8020-assistant/
├── app.py                  # Streamlit UI frontend
├── main.py                 # Flask backend (tool APIs)
├── requirements.txt        # All Python dependencies
├── t8020-bot-v2.jsonl      # Fine-tuning dataset
├── README.md               # Project info
├── .gitignore              # Prevent secrets from being tracked
└── .streamlit/
    └── secrets.toml        # API keys for Streamlit
```

## 🔐 Setting Up Secrets

In `.streamlit/secrets.toml`, store your API keys securely:

```toml
OPENAI_API_KEY = "sk-..."
NEWS_API_KEY = "your_newsapi_key"
GNEWS_API_KEY = "your_gnews_api_key"
ZILLOW_API_KEY = "your_zillow_api_key"
WEATHER_API_KEY = "your_weatherapi_key"
SPORTS_API_KEY = "your_sports_api_key"
```

## ⚙️ Installation & Running Locally

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the Flask API server**:
```bash
python main.py
```

3. **Start the Streamlit frontend**:
```bash
streamlit run app.py
```

## 🧪 Testing the Assistant

Try chatting with prompts like:

- “What’s the weather like in Orlando?”
- “Show me homes for sale in Tampa”
- “Give me NBA scores for today”
- “Tell me the latest news in New York”
- “What’s happening globally right now?”

## 🧠 Fine-Tuning

You can create your own fine-tuned model with the JSONL dataset:

```bash
openai api fine_tunes.create \
  -t t8020-bot-v2.jsonl \
  -m gpt-4-0125-preview
```

Update `app.py` to use your fine-tuned model ID once complete.

## 🛡 Security Notice

✅ **Never commit your secrets or `.streamlit/secrets.toml`**.  
Use `.gitignore` and secret scanning protections provided by GitHub.

## 📤 Deployment

Deploy the backend via Render, Railway, or Heroku.  
Deploy the Streamlit app via [Streamlit Cloud](https://streamlit.io/cloud).

## 🧾 License

MIT License © 2025 [T8020Token Team](https://github.com/T8020Token)
