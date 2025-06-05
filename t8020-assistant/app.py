
import streamlit as st
import openai
import requests
import json

openai.api_key = st.secrets.get("OPENAI_API_KEY")

st.set_page_config(page_title="T8020 Assistant", layout="wide")
st.title("🤖 T8020 Community Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are T8020Bot, a helpful assistant that uses tools."}
    ]

TOOL_ENDPOINTS = {
    "get_current_weather": "http://localhost:5000/get_current_weather",
    "getLocalNews": "http://localhost:5000/getLocalNews",
    "getCommunityEvents": "http://localhost:5000/getCommunityEvents"
}

def call_tool(name, arguments):
    try:
        url = TOOL_ENDPOINTS[name]
        payload = json.loads(arguments)
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

user_input = st.chat_input("Ask T8020Bot something...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
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
                        "name": "getCommunityEvents",
                        "description": "Get community events",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {"type": "string"},
                                "limit": {"type": "integer"}
                            },
                            "required": ["location", "limit"]
                        }
                    }
                }
            ],
            tool_choice="auto"
        )
        message = response["choices"][0]["message"]
        st.session_state.messages.append(message)
        if "tool_calls" in message:
            for tool_call in message["tool_calls"]:
                tool_name = tool_call["function"]["name"]
                args = tool_call["function"]["arguments"]
                result = call_tool(tool_name, args)
                st.session_state.messages.append({"role": "tool", "content": json.dumps(result)})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
