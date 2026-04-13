# 🚀 AutoStream AI Agent

A simple conversational AI agent built for a fictional SaaS platform **AutoStream**.
It interacts with users, answers queries about plans, and captures basic user details for lead generation.

---

## ✨ What this project does

* 💬 Handles user conversations in real-time
* 🧠 Detects user intent (pricing, plans, queries)
* 📦 Suggests suitable subscription plans
* 📝 Collects user details (name, email, platform)
* 🔁 Maintains context across multiple messages

---

## ▶️ How to Run Locally

1. Install dependencies:

```bash id="6jkkxa"
pip install -r requirements.txt
```

2. Create a `.env` file and add your API key:

```text id="9rjbws"
OPENAI_API_KEY=your_api_key_here
```

3. Run the project:

```bash id="4eh37k"
python main.py
```

4. Start chatting in the terminal 🚀

---

## 🧠 Architecture (How it works)

For this project, I used **LangGraph** because it provides a clean way to design conversational flows. Instead of writing a long loop, the chatbot is structured into different steps like intent detection, response handling, and lead collection. This makes the system easier to understand and extend.

Each step acts like a node, and the conversation moves between these nodes based on user input. This approach is closer to how real-world AI agents are built.

State management is handled using LangGraph’s built-in state system. A shared state object stores conversation history and user details such as name and email. Because of this, the agent can remember context across multiple turns (around 5–6 messages) and respond more naturally without losing track of the conversation.

---

## 📱 WhatsApp Integration (Concept)

To deploy this agent on WhatsApp, we can use the **WhatsApp Business API** with webhooks.

* When a user sends a message, it is received by a webhook (backend server).
* The webhook forwards the message to the AI agent.
* The agent processes the input and generates a response.
* The response is sent back to the user through the WhatsApp API.

This requires:

* A backend server (Flask or FastAPI)
* Webhook endpoint
* WhatsApp API integration (via Meta or Twilio)

This setup enables real-time chatbot interaction on WhatsApp.

---

## 🛠️ Tech Stack

* Python
* LangChain + LangGraph
* OpenAI (GPT-4o-mini)
* JSON (knowledge base)

---

## 📂 Project Structure

```text id="kxv5hd"
project/
│── main.py
│── knowledge.json
│── requirements.txt
│── .gitignore
│── README.md
```

---

## 👩‍💻 Author

Poornima Paidy
Computer Science & Engineering (AI)

