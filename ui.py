# ui.py
import streamlit as st
import requests

st.write("✅ UI is running")

API_URL = st.secrets.get("API_URL", "https://rag-with-guardrails-production.up.railway.app/chat")

st.write(f"🔗 Using API_URL: {API_URL}")

st.title("RAG Chatbot with Guardrails")
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_input("Ask me something:")

if st.button("Send") and user_input:
    payload = {"session_id": "demo", "question": user_input}
    resp = requests.post(API_URL, json=payload)
    answer = resp.json().get("answer", "[no answer]")

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", answer))

# Show history
for role, msg in st.session_state.history:
    st.markdown(f"**{role}:** {msg}")
