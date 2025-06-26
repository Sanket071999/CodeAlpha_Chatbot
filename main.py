import time
import random

# Typing simulation
def bot_reply(message):
    print("MiniGPT is typing...", end="\r")
    time.sleep(random.uniform(0.6, 1.2))
    print("🤖 MiniGPT:", message)

# Response generator
def get_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return random.choice(["Hey there!", "Hello 👋", "Hi! How can I help you today?"])
    elif "how are you" in user_input:
        return "I'm all good! How about you?"
    elif "your name" in user_input:
        return "I'm MiniGPT – your pocket-sized assistant 🤖"
    elif "what can you do" in user_input:
        return "I can chat, joke, and keep you entertained a little! Want to try?"
    elif "joke" in user_input:
        return random.choice([
            "Why don’t scientists trust atoms? Because they make up everything!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why did the computer go to therapy? It had too many bytes of sadness 😅"
        ])
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Chat with you soon 👋"
    else:
        return "Hmm... I didn't quite get that. Try saying something else?"

# Chat loop
def interactive_chatbot():
    bot_reply("Hi! I'm MiniGPT 🤖. Let's chat! (Type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        bot_reply(response)

        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

# Start chatting
interactive_chatbot()
