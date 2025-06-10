# 🤖 ChatSquire

Your trusty command-line AI assistant powered by OpenAI's GPT-4.

**ChatSquire** is a lightweight, terminal-based chatbot that delivers intelligent, conversational responses using the OpenAI API. Whether you're brainstorming, learning, or just curious, ChatSquire is always at your service — like a loyal squire of code.

---

## 🛡️ Features

- 💬 Maintains context-aware conversations.
- 🔐 Simple API key configuration.
- ⚙️ Easy to extend and customize.
- 📦 Minimal dependencies, CLI-only setup.

---

## 🗂️ Folder Structure

ChatSquire/
│
├── ai_chatbot.py # Main chatbot with conversation memory
├── main.py # Single prompt-response demo
├── config.py # API key storage
├── requirements.txt # Dependencies
└── README.md # You're here!

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ChatSquire.git
cd ChatSquire
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add Your OpenAI API Key
Edit the config.py file:

python
Copy
Edit
Api_key = "your_openai_api_key_here"
4. Start ChatSquire (Interactive)
bash
Copy
Edit
python ai_chatbot.py
You’ll be greeted by the Squire and can begin chatting right away.

5. Use Single Prompt Mode (Demo)
bash
Copy
Edit
python main.py
This sends one hardcoded prompt and prints the result.

🧠 Example Session
bash
Copy
Edit
Assistant: Hi I am available, How may I help you...

User: What are some good Python projects?
Assistant: Here are a few beginner-friendly Python projects you can try...
📝 Docstrings and Code Quality
Custom exceptions like NoKey for missing API key.

Each function includes Pythonic docstrings.

Easy to extend for logging, saving chat history, or GUI integrations.

🔑 Keywords
OpenAI GPT-4 Chatbot AI Assistant CLI Tool Python ChatSquire Prompt Engineering Terminal AI

📃 License
MIT License — feel free to use and adapt.

🤔 Future Enhancements (Optional Ideas)
Save chat history to a file.

Add GUI (Tkinter/Streamlit).

Switch models via config.

Integrate with speech-to-text APIs.

Let your ideas come to life. ChatSquire is here to serve.

yaml
Copy
Edit

---
