from agent.intent_detector import detect_intent
from agent.tool_executor import execute_tool
from rag.retriever import retrieve_context

class SalesAgent:
    def __init__(self):
        self.state = {}

    def run(self, user_query: str):

        # 1. Intent Detection
        intent = detect_intent(user_query)

        # 2. RAG Context Retrieval
        context = retrieve_context(user_query)

        # 3. Tool Execution Layer
        tool_result = execute_tool(intent, user_query)

        # 4. Response Fusion (simple reasoning layer)
        response = self.generate_response(context, tool_result, user_query)

        return response

    def generate_response(self, context, tool_result, query):
        return f"""
Based on your query: {query}

📦 Product Context:
{context}

🛠 Tool Output:
{tool_result}

💡 Recommendation:
I suggest choosing the option that best fits your requirements from the above results.
"""
