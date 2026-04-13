class StateManager:
    def __init__(self):
        # Stores conversation history or context
        self.state = {
            "history": [],
            "user_preferences": {}
        }

    def add_message(self, role, message):
        self.state["history"].append({
            "role": role,
            "message": message
        })

    def get_history(self):
        return self.state["history"]

    def set_preference(self, key, value):
        self.state["user_preferences"][key] = value

    def get_preference(self, key):
        return self.state["user_preferences"].get(key, None)

    def clear_state(self):
        self.state = {
            "history": [],
            "user_preferences": {}
        }
