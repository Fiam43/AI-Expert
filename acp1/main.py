import random
import datetime

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi CodrX!"],
    "how are you": ["I'm fine!", "Doing great!", "Awesome!", "I'm just code, but I'm happy!"],
    "what is your name": ["I'm your AI chatbot.", "You can call me PyBot!", "I am CodrX's assistant."],
    "who created you": ["I was created using Python.", "A smart coder built me 😉", "CodrX is improving me!"],
    "what can you do": ["I can chat with you!", "I can answer simple questions.", "I am learning more every day!"],
    "tell me a joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the computer cold? It forgot to close Windows!",
        "I would tell you a UDP joke, but you might not get it."
    ],
    "favourite sport": ["I like football!", "Cricket is awesome!", "All sports are cool!"],
    "time": ["Let me check the time..."],
    "date": ["Let me check today's date..."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
}

print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "time" in user_input:
        now = datetime.datetime.now()
        print("AI Chatbot: Current time is", now.strftime("%H:%M:%S"))
        continue

    if "date" in user_input:
        today = datetime.date.today()
        print("AI Chatbot: Today's date is", today)
        continue

    if user_input == "bye":
        print("AI Chatbot:", random.choice(responses["bye"]))
        break

    found = False
    for key in responses:
        if key in user_input:
            print("AI Chatbot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("AI Chatbot: Sorry, I don't understand that yet. I'm still learning!")