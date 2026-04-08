import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket", "Boracay"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Mount Fuji"],
    "cities": ["Tokyo", "Paris", "New York", "Dubai"]
}

jokes = [
    "Why don't scientists trust atoms? Because they make up everything.",
    "What do you call a fake noodle? An impasta.",
    "What do you call a bear with no teeth? A gummy bear."
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            suggestion = random.choice(destinations[preference])
            print(Fore.GREEN + f"TravelBot: Maybe try {suggestion} instead!")
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "- Type 'exit' or 'bye' to end.\n")

def weather():
    print(Fore.CYAN + "TravelBot: Which city?")
    city = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: I recommend checking the weather for {city} before traveling!")

facts = [
    "The shortest flight in the world lasts only 57 seconds.",
    "France is the most visited country in the world.",
    "The Maldives has around 1200 islands."
]

def travel_fact():
    print(Fore.GREEN + random.choice(facts))

def chat():
    print(Fore.CYAN + "TravelBot: Hi! I'm your travel assistant. How can I help you today?")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + "You: ")
        user_input = normalize_input(user_input)

        if user_input in ["exit", "bye"]:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        elif any(word in user_input for word in ["recommend", "travel", "place", "destination"]):
            recommend()
        elif "packing" in user_input:
            packing_tips()
        elif "joke" in user_input:
            tell_joke()
        elif "weather" in user_input:
            weather()
        elif "fact" in user_input:
            travel_fact()
        else:
            print(Fore.RED + "TravelBot: Sorry, I didn't understand that. Please try again.")
            show_help()

if __name__ == "__main__":
    chat()



            