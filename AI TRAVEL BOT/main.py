import tkinter as tk
from tkinter import scrolledtext
import random
import re
import requests
from textblob import TextBlob

# -------------------
# DATA
# -------------------

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket", "Hawaii"],
    "mountains": ["Swiss Alps", "Himalayas", "Rocky Mountains"],
    "cities": ["Tokyo", "Paris", "Dubai", "New York"]
}

jokes = [
    "Why did the airplane go to school? To improve its altitude!",
    "Why don't scientists trust atoms? Because they make up everything!"
]

facts = [
    "France is the most visited country in the world.",
    "The Maldives has around 1200 islands.",
    "Dubai has the tallest building in the world."
]

tips = [
    "Always carry a portable charger.",
    "Pack light and smart.",
    "Keep digital copies of your documents."
]

history = []

# -------------------
# TEXT UTILITIES
# -------------------

def normalize(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def mood(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0:
        return "You sound excited! 😊"
    elif score < 0:
        return "Maybe a vacation would help!"
    else:
        return "Let's plan a trip!"

# -------------------
# WEATHER
# -------------------

def weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        return requests.get(url).text
    except:
        return "Weather service unavailable."

# -------------------
# MAP LINK
# -------------------

def map_link(place):
    return f"https://www.google.com/maps/search/{place}"

# -------------------
# FLIGHT SIMULATION
# -------------------

def fake_flight():
    airlines = ["SkyTravel", "GlobalAir", "JetWorld"]
    price = random.randint(300, 1200)
    airline = random.choice(airlines)

    return f"Flight found: {airline} - ${price}"

# -------------------
# CHATBOT
# -------------------

def respond(user):

    text = normalize(user)

    response = mood(user) + "\n"

    if "recommend" in text:

        category = random.choice(list(destinations.keys()))
        place = random.choice(destinations[category])

        history.append(place)

        response += f"I recommend visiting {place}\n"
        response += "Map: " + map_link(place)

    elif "weather" in text:

        city = text.split()[-1]
        response += weather(city)

    elif "flight" in text:

        response += fake_flight()

    elif "packing" in text:

        response += "\nPacking tips:\n"
        response += "- Pack versatile clothes\n"
        response += "- Bring chargers\n"
        response += "- Carry travel documents"

    elif "joke" in text:

        response += random.choice(jokes)

    elif "fact" in text:

        response += random.choice(facts)

    elif "tip" in text:

        response += random.choice(tips)

    elif "history" in text:

        if history:
            response += "\nTravel suggestions so far:\n"
            for h in history:
                response += "- " + h + "\n"
        else:
            response += "No travel history yet."

    else:

        response += "Try commands: recommend, weather city, flight, packing, joke, fact, tip."

    return response

# -------------------
# GUI
# -------------------

def send():

    user = entry.get()
    entry.delete(0, tk.END)

    chat.insert(tk.END, "You: " + user + "\n")

    reply = respond(user)

    chat.insert(tk.END, "TravelBot: " + reply + "\n\n")

window = tk.Tk()
window.title("God-Level Travel AI Assistant")
window.geometry("540x640")

title = tk.Label(window, text="🌍 God-Level Travel AI Assistant", font=("Arial",18))
title.pack(pady=10)

chat = scrolledtext.ScrolledText(window,width=60,height=25)
chat.pack(pady=10)

entry = tk.Entry(window,width=40)
entry.pack(pady=5)

send_btn = tk.Button(window,text="Send",command=send)
send_btn.pack()

window.mainloop()