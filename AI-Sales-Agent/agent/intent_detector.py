def detect_intent(query: str):

    query = query.lower()

    if "buy" in query or "price" in query:
        return "product_search"

    elif "order" in query:
        return "order_tracking"

    elif "help" in query or "how" in query:
        return "faq"

    else:
        return "general_chat"
