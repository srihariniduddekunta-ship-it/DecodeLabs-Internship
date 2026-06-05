print("Welcome to AI Chatbot!")
while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! How can I help you today?")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: My name is AI Assistant.")

    elif user == "who created you":
        print("Bot: I was created as a rule-based chatbot project.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language used for AI, web development, and more.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence, which enables machines to simulate human intelligence.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "good morning":
        print("Bot: Good morning! Have a wonderful day.")

    elif user == "good night":
        print("Bot: Good night! Sleep well.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")