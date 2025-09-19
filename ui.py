# ui.py
import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

st.write("✅ Streamlit app is running")
API_URL = st.secrets.get("API_URL", "https://rag-with-guardrails-production.up.railway.app/chat")

st.title("RAG Chatbot with Guardrails")

# --- Initialize history ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# --- Display chat history ---
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat input (native Streamlit chat UI) ---
if prompt := st.chat_input("Ask me something:"):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to backend
    try:
        resp = requests.post(
            API_URL,
            json={"session_id": "demo", "question": prompt},
            timeout=30,
        )
        resp.raise_for_status()
        answer = resp.json().get("answer", "Sorry, I couldn't process your request.")
    except requests.exceptions.RequestException as e:
        answer = f"❌ Error calling API: {e}"

    # Add bot message
    st.session_state["messages"].append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
