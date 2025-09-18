# 🤖 RAG Chatbot UI (Streamlit)

A simple **Streamlit frontend** for the [RAG with Guardrails backend](https://github.com/Ali-Ismail-1/RAG-with-guardrails).  
This UI connects to the FastAPI service and lets you chat with the RAG pipeline in a clean, chat-style interface.

👉 **Live Demo**: https://rag-app-ui-ai.streamlit.app/

---

## 📂 Project Structure
```
rag-streamlit-ui/
├── ui.py # Main Streamlit app
├── requirements.txt # Dependencies
├── .gitignore
```

---

## 🚀 Run Locally
```bash
git clone https://github.com/ali-ismail-1/rag-streamlit-ui.git
cd rag-streamlit-ui
pip install -r requirements.txt
streamlit run ui.py
```

Then open http://localhost:8501 in your browser.

---

## 🛠 Tech Stack
- Streamlit — frontend framework
- Requests — API calls
- FastAPI backend (hosted on Railway)
