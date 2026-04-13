def faq_response(query: str):
    faqs = {
        "return policy": "You can return items within 7 days.",
        "payment": "We support UPI, cards, and COD.",
        "shipping": "Shipping takes 3-5 business days."
    }

    for key in faqs:
        if key in query.lower():
            return faqs[key]

    return "Sorry, I couldn't find an answer. Please contact support."
