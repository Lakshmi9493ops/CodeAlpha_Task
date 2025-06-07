
def chatbot_reply(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great, thanks for asking! 😊"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Take care!"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple chatbot created by a B.Tech student!"
    elif user_input in ["what can you do", "help"]:
        return "I can respond to basic greetings and questions. Try saying 'hello' or 'how are you'."
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"
    elif user_input in ["what is python"]:
        return "Python is a powerful programming language that's great for beginners and pros alike!"
    elif user_input in ["tell me a joke"]:
        return "Why do programmers prefer dark mode? Because the light attracts bugs! 🐛"
    else:
        return "I'm still learning! Can you try something else?"

def chatbot():
    print("🤖 Welcome to B.Tech ChatBot!")
    print("Type something like 'hello', 'how are you', 'bye', or 'help'. Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        response = chatbot_reply(user_input)
        print("Chatbot:", response)

chatbot()
