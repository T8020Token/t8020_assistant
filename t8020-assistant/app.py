import streamlit as st
import requests
import json
from openai import OpenAI

# OpenAI client using secret key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="T8020 Assistant", layout="wide")
st.title("🤖 T8020 Community Assistant")

# Initialize chat state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are T8020Bot, a helpful assistant that uses real-time tools."}
    ]

# Define backend tool routes
TOOL_ENDPOINTS = {
    "get_current_weather": "http://localhost:5000/get_current_weather",
    "getLocalNews": "http://localhost:5000/getLocalNews",
    "getNationalNews": "http://localhost:5000/getNationalNews",
    "getWorldNews": "http://localhost:5000/getWorldNews",
    "getLocalSportsScores": "http://localhost:5000/getLocalSportsScores",
    "getNationalSportsUpdates": "http://localhost:5000/getNationalSportsUpdates",
    "getZillowListings": "http://localhost:5000/getZillowListings",
    "getGNewsWorld": "http://localhost:5000/getGNewsWorld"
}

# Function to call a tool endpoint
def call_tool(name, arguments):
    try:
        url = TOOL_ENDPOINTS[name]
        payload = json.loads(arguments)
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Chat input
user_input = st.chat_input("Ask T8020Bot something...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o",  # or your fine-tuned model ID
            messages=st.session_state.messages,
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "get_current_weather",
                        "description": "Get the current weather",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {"type": "string"},
                                "format": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                            },
                            "required": ["location", "format"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "getLocalNews",
                        "description": "Fetch local news",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {"type": "string"},
                                "category": {"type": "string"},
                                "limit": {"type": "integer"}
                            },
                            "required": ["location", "category", "limit"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "getNationalNews",
                        "description": "Fetch national news",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "category": {"type": "string"},
                                "limit": {"type": "integer"}
                            },
                            "required": ["category", "limit"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "getWorldNews",
                        "description": "Get latest world news",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "limit": {"type": "integer"}
                            },
                            "required": ["limit"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "getLocalSportsScores",
                        "description": "Get local sports results",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "team": {"type": "string"},
                                "sport": {"type": "string"},
                                "date": {"type": "string"}
                            },
                            "required": ["team", "sport", "date"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "getNationalSportsUpdates",
                        "description": "Get national sports updates",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "league": {"type": "string"},
                                "date": {"type": "string"}
                            },
                            "required": ["league", "date"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "getZillowListings",
                        "description": "Search Zillow for listings",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {"type": "string"},
                                "priceMin": {"type": "integer"},
                                "priceMax": {"type": "integer"},
                                "propertyType": {"type": "string"}
                            },
                            "required": ["location", "priceMin", "priceMax", "propertyType"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "getGNewsWorld",
                        "description": "Get world news via GNews API",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "topic": {"type": "string"},
                                "limit": {"type": "integer"}
                            },
                            "required": ["topic", "limit"]
                        }
                    }
                }
            ],
            tool_choice="auto"
        )

        message = response.choices[0].message
        st.session_state.messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                args = tool_call.function.arguments
                result = call_tool(tool_name, args)
                st.session_state.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result, indent=2)
                })

# Render chat messages
for msg in st.session_state.messages:
    if "role" in msg and "content" in msg:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
