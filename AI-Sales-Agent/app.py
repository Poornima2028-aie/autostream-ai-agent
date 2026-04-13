from agent.agent_core import SalesAgent

def main():
    agent = SalesAgent()

    print("AI Sales Assistant is running... Type 'exit' to stop")

    while True:
        user_input = input("\nUser: ")

        if user_input.lower() == "exit":
            break

        response = agent.run(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()
