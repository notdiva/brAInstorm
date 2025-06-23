# 🤖 brAInstorm buddy

**brAInstorm buddy** is an AI-powered brainstorming assistant built with **Streamlit** and **OpenRouter (OpenAI-compatible API)**. Just type in your startup idea or problem statement, and instantly receive:

✅ 7 creative and brandable **product names**  
✅ 4 catchy **taglines**  
✅ 3 viable **business model** ideas  
✅ 3 clever **launch strategies**

---

## 🚀 Live Demo

Try it here: [https://brainstormbuddy.streamlit.app/](https://brainstormbuddy.streamlit.app/)

---

## 🛠 Features

- ✨ Clean and minimal Streamlit UI  
- 💡 AI-generated creative ideas using **Mixtral-8x7B-Instruct** model  
- 🔐 Secure API key handling using `st.secrets`  
- 🌍 Uses [OpenRouter.ai](https://openrouter.ai) for flexible model support  

---
📁 Project Structure
```bash
brainstorm-buddy/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── .streamlit/
    └── secrets.toml        # Secure API key storage
```
---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/brainstorm-buddy.git
cd brainstorm-buddy
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a .streamlit/secrets.toml file
```bash
OPENROUTER_API_KEY = "your_openrouter_api_key_here"
```
### 4. Run the app

```bash
streamlit run app.py
```
