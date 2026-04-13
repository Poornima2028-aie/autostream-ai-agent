from tools.product_search import search_products
from tools.order_tool import track_order
from tools.faq_tool import faq_response

def execute_tool(intent, query):

    if intent == "product_search":
        return search_products(query)

    elif intent == "order_tracking":
        return track_order(query)

    elif intent == "faq":
        return faq_response(query)

    else:
        return "No tool needed. Handling via LLM response layer."
