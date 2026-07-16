print("Hello, I am ChatBot! What is your name?")
name = input()
print(f"I feel very nice meeting you, {name}!")

print("Ok so what is your mood today? (good/bad)")
mood = input()
if mood == "good":
    print("That's great to hear!")
    print("Do you like to hear songs? (yes/no)")
    song_preference = input().strip().lower()
    if song_preference == "yes":
        print("Great!")
    elif song_preference == "no":
        print("No problem! Let's talk about something else.")
    else:
        print("I see. Sometimes it's hard to make decisions.")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon!")
    print("I can tell you a joke to cheer you up! Do you want to hear one? (yes/no)")
    joke_preference = input().strip().lower()
    if joke_preference == "yes":
        print("Why don't scientists trust atoms?")
        print("Because they make up everything!")
    elif joke_preference == "no":
        print("No problem! Let's talk about something else.")
    else:
        print("I see. Sometimes it's hard to make decisions.")
else:
    print("I see. Sometimes its hard to put feelings into words.")

print(f"I had a nice time talking to you, {name}. Goodbye!")