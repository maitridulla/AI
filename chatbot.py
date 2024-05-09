def elementary_chatbot():
    print("Hello! I'm your elementary chatbot.")
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a computer program, but thanks for asking!")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "favorite color" in user_input:
            print("Chatbot: I don't have a favorite color. What's yours?")
            user_color = input("You: ")
            print(f"Chatbot: {user_color} is a nice color!")

        else:
            print("Chatbot: I'm not sure how to respond. Can you rephrase that or ask something else?")

if __name__ == "__main__":
    elementary_chatbot()
