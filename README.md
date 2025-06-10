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


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ChatSquire.git
cd ChatSquire

2. Install Dependencies

pip install -r requirements.txt

3. Add Your OpenAI API Key
Edit the config.py file:

Api_key = "your_openai_api_key_here"

4. Start ChatSquire (Interactive)
python ai_chatbot.py
You’ll be greeted by the Squire and can begin chatting right away.

5. Use Single Prompt Mode (Demo)
python main.py
This sends one hardcoded prompt and prints the result.

🧠 Example Session
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


---

Let me know if you'd like a stylized logo (ASCII or image), badge icons (e.g., "Built with OpenAI", "MIT License"), or a GitHub Actions workflow for linting or CI.
