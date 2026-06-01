print("=" * 50)
print("Rule-Based AI Chatbot")
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user_input in ["who are you", "what is your name"]:
        print("Bot: I am a Rule-Based AI chatbot designed to answer predefined user queries.")

    elif user_input == "what is ai":
        print("Bot: AI (Artificial Intelligence) is the simulation of human intelligence by machines.")

    elif user_input == "python":
        print("Bot: Python is a popular programming language widely used in AI and Machine Learning.")

    elif user_input == "help":
        print("\nAvailable Commands:")
        print("- hi")
        print("- hello")
        print("- who are you")
        print("- what is ai")
        print("- python")
        print("- help")
        print("- exit")

    elif user_input in ["exit", "bye", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")