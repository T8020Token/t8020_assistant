import streamlit as st
import openai
import requests
import json

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="T8020 Assistant", layout="wide")
st.title("🤖 T8020 Community Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are T8020Bot, a smart assistant that uses real-time tools to get data."}
    ]

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

def call_tool(name, arguments):
    try:
        url = TOOL_ENDPOINTS[name]
        payload = json.loads(arguments)
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

user_input = st.chat_input("Ask T8020Bot anything...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",  # Or your fine-tuned model
            messages=st.session_state.messages,
            tools=[...],  # tool definitions go here (use earlier tool schema)
            tool_choice="auto"
        )
        message = response["choices"][0]["message"]
        st.session_state.messages.append(message)
        if "tool_calls" in message:
            for tool_call in message["tool_calls"]:
                tool_name = tool_call["function"]["name"]
                args = tool_call["function"]["arguments"]
                result = call_tool(tool_name, args)
                st.session_state.messages.append({"role": "tool", "content": json.dumps(result, indent=2)})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
