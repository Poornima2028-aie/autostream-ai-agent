import os
import requests
from dotenv import load_dotenv
from typing import TypedDict
from langgraph.graph import StateGraph, END

# ---------------- LOAD ENV ----------------
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# ---------------- LLM ----------------
def ask_llm(prompt):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

# ---------------- STATE ----------------
class AgentState(TypedDict):
    user_input: str
    intent: str
    stage: str
    name: str
    email: str
    platform: str
    response: str

# ---------------- KNOWLEDGE ----------------
def get_knowledge():
    return """
Pricing:
Basic: $29/month
Pro: $79/month

Policies:
No refunds after 7 days
24/7 support for Pro users
"""

# ---------------- NODES ----------------

def detect_intent(state: AgentState):
    prompt = f"""
Classify intent into:
greeting / info / high_intent

Message: {state['user_input']}

Answer only one word.
"""
    state["intent"] = ask_llm(prompt).strip().lower()
    return state


def handle_conversation(state: AgentState):

    # Lead capture flow
    if state.get("stage") == "ask_name":
        state["name"] = state["user_input"]
        state["stage"] = "ask_email"
        state["response"] = "Enter your email:"
        return state

    elif state.get("stage") == "ask_email":
        state["email"] = state["user_input"]
        state["stage"] = "ask_platform"
        state["response"] = "Which platform do you use?"
        return state

    elif state.get("stage") == "ask_platform":
        state["platform"] = state["user_input"]
        print(f"\n✅ Lead captured: {state['name']}, {state['email']}, {state['platform']}\n")
        state["stage"] = None
        state["response"] = "Thank you! 🎉"
        return state

    # Normal flow
    if "greeting" in state["intent"]:
        state["response"] = "Hello! 👋"

    elif "info" in state["intent"]:
        prompt = f"""
Use this info:

{get_knowledge()}

Answer: {state['user_input']}
"""
        state["response"] = ask_llm(prompt)

    elif "high_intent" in state["intent"]:
        state["stage"] = "ask_name"
        state["response"] = "Great! What's your name?"

    else:
        state["response"] = "I didn't understand."

    return state

# ---------------- GRAPH ----------------
builder = StateGraph(AgentState)

builder.add_node("intent", detect_intent)
builder.add_node("conversation", handle_conversation)

builder.set_entry_point("intent")
builder.add_edge("intent", "conversation")
builder.add_edge("conversation", END)

graph = builder.compile()

# ---------------- RUN ----------------
def run_chat():
    print("🤖 AutoStream AI Agent (LangGraph) Started")
    print("Type 'exit' to quit\n")

    state = {
        "stage": None,
        "name": "",
        "email": "",
        "platform": ""
    }

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        state["user_input"] = user_input

        state = graph.invoke(state)

        print("Agent:", state["response"])


if __name__ == "__main__":
    run_chat()