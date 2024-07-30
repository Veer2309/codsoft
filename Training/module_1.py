# CHATBOT WITH RULE-BASED RESPONSES Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This will give you a basic understanding of natural language processing and conversation flow.

responses = {
    "hi": "Hello! How can I help you today?",
    "hey": "Hey there! What can I do for you?",
    "hello": "Hi! What's on your mind?",
    "how are you": "I'm good, thank you! How about you?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "what is your name" : " I am a bot.How can I help you! ",
    "who is your creator" :"I am created by my developer name Veer Sharma",
    "for any complain contact details" : "sharmaveer2005@gmail.com or
     7300323553",
    "default": "I'm sorry, I didn't understand that.",
}

def respond(message):
    # Convert the message to lowercase
    
    message = message.lower()
    
    # Check for patterns and select response

    if message in responses:
        return responses[message]
    else:
        return responses["default"]

    print("Welcome! Type 'bye' to exit.")

    while True:
        user_message = input("You: ")

        if user_message.lower() == 'bye':
            print(responses["bye"])
            break
        else:
            bot_response = respond(user_message)
            print("Bot:", bot_response)
