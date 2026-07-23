import re, random
from colorama import Fore, init
init(autoreset=True)

destinations = {
    "beaches": ["Maldives", "Bali", "Hawaii", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes"],
    "cities": ["New York", "Paris", "Tokyo", "London"],
}

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the math book look sad? Because it had too many problems.",
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "What type of destination are you interested in? (beaches, mountains, cities)")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: I recommend visiting {suggestion}!")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + "TravelBot: Great! I'm sure you'll have a wonderful time.")
        elif answer == "no":
            print(Fore.GREEN + "TravelBot: No problem! Lets try another option.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I didn't understand that. Let's try again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have recommendations for that type of destination.")

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + f"TravelBot: How many days?:")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.CYAN + f"TravelBot: Here are some packing tips for your {days}-day trip to {location}:")
    print(Fore.GREEN + "- Make a checklist of essentials.")
    print(Fore.GREEN + "- Pack versatile clothing.")
    print(Fore.GREEN + "- Don't forget chargers and adapters.")
    print(Fore.GREEN + "- Keep important documents in a safe place.")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\n Can:")
    print(Fore.GREEN + "- Recommend a travel destination(say 'recommendation')")
    print(Fore.GREEN + "- Provide packing tips(say 'packing')")
    print(Fore.GREEN + "- Tell a joke(say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'end' to leave the chat.\n")

def chat():
    print(Fore.CYAN + "TravelBot: Hello! I'm your travel assistant.")
    name = input(Fore.YELLOW + "TravelBot: What's your name? ")
    print(Fore.GREEN + f"TravelBot: Nice to meet you, {name}! ")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        normalized_input = normalize_input(user_input)

        if "recommend" in user_input:
            recommend()
        elif "packing" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "end" in user_input:
            print(Fore.CYAN + "TravelBot: Goodbye! Safe travels!")
            break
        else:
            print(Fore.RED + "TravelBot: I'm sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chat()