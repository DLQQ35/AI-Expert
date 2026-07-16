import webbrowser

print("Hello, I am AI Bot! What is your name?")
name = input().strip()
print(f"Nice to meet you, {name}!")
print("I can open a web page for you. What website would you like to visit? (e.g.,youtube, google, wikipedia)")
website = input().strip().lower()
url = f"https://www.{website}.com"
print(f"Opening {url} for you, {name}!")
webbrowser.open(url)

print(f"I had a nice time talking to you, {name}. Goodbye!")