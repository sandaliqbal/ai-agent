# LangGraph + Ollama Streaming Chatbot

A minimal example showing how to build a streaming chatbot using:

- **LangGraph** (for agent workflows)
- **Ollama** (local LLMs)
- **Tool calling**
- **In-memory conversation thread storage**
- **Gradio UI (frontend optional)**

This project demonstrates:
- A simple agent node
- Automatic routing to tools
- Streaming outputs
- Per-session conversation memory using `thread_id`

---

## 🚀 Features

- Local LLM (Ollama)
- Tool calling with LangChain / LangGraph
- Conversation memory per browser session
- Supports streaming token updates
- Very small, readable codebase

---

## 📁 Project Structure

```text
.
├── agent.py          # Main graph logic
├── agent_state.py    # Defines state schema for LangGraph
├── tools.py          # Example tools (e.g., check_weather)
├── test_agent.py     # Test agent code
└── README.md
```


---

## 📦 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the agent

```bash
python src/test_agent.py
```

## License

MIT License.

## Credits

Built with:

- LangGraph
- LangChain
- Ollama
