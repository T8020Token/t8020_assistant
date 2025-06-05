
# T8020 Assistant

This is an AI assistant built with OpenAI, Streamlit, and Flask that supports tool calling.

## 🔧 Setup

```bash
git clone https://github.com/yourusername/t8020-assistant.git
cd t8020-assistant
pip install -r requirements.txt
```

## 🔑 Add Your OpenAI Key

Edit `.streamlit/secrets.toml` and add:
```toml
OPENAI_API_KEY = "your-openai-key"
```

## 🚀 Run Locally

Start the backend server (tool API):
```bash
python main.py
```

Then start the Streamlit UI:
```bash
streamlit run app.py
```

Go to: http://localhost:8501

## 🎯 Fine-Tuning

You can upload `mydata_fixed.jsonl` to OpenAI for custom fine-tuning.

