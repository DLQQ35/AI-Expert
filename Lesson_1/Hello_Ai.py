print("Hello, I am AI Bot! What is your name?")
name = input()
print(f"Nice to meet you, {name}!")

print("How are you feeling today?(good/bad)")
mood = input()
if mood == "good":
    print("That's great to hear!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon!")
else:
    print("I see. Sometimes its hard to put feelings into words.")

print(f"I had a nice time talking to you, {name}. Goodbye!")