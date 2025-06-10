# 🤖 ChatSquire

**ChatSquire** is your loyal command-line chatbot powered by OpenAI's GPT-4.

Built for simplicity, clarity, and conversation, ChatSquire is a lightweight Python assistant designed to answer your queries, assist with brainstorming, and provide instant responses — all from your terminal.

---

## 🛠️ Features

- 💬 Context-aware conversation handling
- 🔐 Simple API key setup using `config.py`
- 🧩 Modular code and easy to extend
- 🖥️ Purely terminal-based, no UI required

---

## 📂 Project Structure

```
ChatSquire/
├── ai_chatbot.py       # Main chatbot with multi-turn conversation
├── main.py             # Demo script for single prompt-response
├── config.py           # Stores OpenAI API key
├── requirements.txt    # Python dependencies
└── README.md           # Project overview and setup
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ChatSquire.git
cd ChatSquire
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Set Your OpenAI API Key

Open the `config.py` file and paste your OpenAI API key:

```python
API_KEY = "your_openai_api_key_here"
```

---

## 🧠 How to Use

### 🔁 Start the Interactive Chatbot

```bash
python ai_chatbot.py
```

You’ll be greeted by ChatSquire and can begin chatting.

### 💡 One-Time Prompt (Demo Script)

```bash
python main.py
```

This sends a single hardcoded question and prints the GPT-4 response.

---

## 📌 Example Session

```bash
Assistant: Hi I am available, How may I help you...

User: What is Python?
Assistant: Python is a high-level, interpreted programming language...
```

---

## 🧾 Requirements

- Python 3.7+
- OpenAI Python SDK

Install dependencies:

```bash
pip install openai
```

---

## 📄 Code Overview

- `ai_chatbot.py`: Maintains conversation history, handles user input, and prints assistant responses.
- `main.py`: Quick demo with a static question.
- `config.py`: Holds the API key.
- Uses a custom `NoKey` exception for clear error handling.

---

## 📝 Keywords

`OpenAI` `GPT-4` `Python` `Chatbot` `Terminal Assistant` `AI` `Prompt Engineering` `ChatSquire`

---

## 📃 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

---

## 🛡️ Future Enhancements

- Save conversation history to a file
- Add support for switching between GPT models
- Basic GUI using Streamlit or Tkinter
- Integrate voice input/output

---

## 💬 Final Note

Let your ideas come to life — one prompt at a time.  
**ChatSquire is here to serve.**
