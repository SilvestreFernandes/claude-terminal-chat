# 🤖 Claude Terminal Chat

A conversational AI chatbot that runs directly in your terminal, powered by **Anthropic's Claude API**.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Anthropic](https://img.shields.io/badge/Powered%20by-Claude%20API-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 💬 Multi-turn conversation with memory (keeps full chat history)
- 🌍 Bilingual — responds in Portuguese or English automatically
- 🎨 Colorful terminal interface
- 📜 View chat history anytime
- 🧹 Clear conversation history on the fly
- ⚡ Built with the official Anthropic Python SDK

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SilvestreFernandes/claude-terminal-chat.git
cd claude-terminal-chat
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your API Key

Get your API key at [console.anthropic.com](https://console.anthropic.com).

**Option A — Environment variable (recommended):**

Linux / macOS:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Windows CMD:
```cmd
set ANTHROPIC_API_KEY=your-api-key-here
```

Windows PowerShell:
```powershell
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

> ⚠️ Set the variable in the **same terminal window** you'll run the script in.

**Option B — Edit the file directly:**

Open `chat.py` and replace `"sua-api-key-aqui"` with your key.

### 4. Run

```bash
python chat.py
```

---

## 🕹️ Commands

| Command | Description |
|---|---|
| `sair` / `exit` | End the chat |
| `limpar` / `clear` | Clear conversation history |
| `historico` / `history` | Show previous messages |

---

## 📁 Project Structure

```
claude-terminal-chat/
├── chat.py           # Main chatbot script
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```

---

## 🛠️ Built With

- [Python 3.8+](https://www.python.org/)
- [Anthropic Python SDK](https://github.com/anthropic-ai/anthropic-sdk-python)

---

## 👤 Author

**Silvestre Fernandes**  
[![GitHub](https://img.shields.io/badge/GitHub-SilvestreFernandes-black?logo=github)](https://github.com/SilvestreFernandes)

---

## 📄 License

This project is licensed under the MIT License.