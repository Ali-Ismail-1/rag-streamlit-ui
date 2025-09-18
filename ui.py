# ui.py
import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

# Debug info
st.write("✅ Streamlit app is running")
API_URL = st.secrets.get("API_URL", "https://rag-with-guardrails-production.up.railway.app/chat")
st.write(f"🔗 Using API_URL: {API_URL}")

st.title("RAG Chatbot with Guardrails")

# Input
user_input = st.text_input("Ask me something:")

if st.button("Send") and user_input:
    try:
        resp = requests.post(API_URL, json={"session_id": "demo", "question": user_input}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        st.success(f"Bot: {data.get('answer', '[no answer in response]')}")
    except Exception as e:
        st.error(f"❌ Error calling API: {e}")
