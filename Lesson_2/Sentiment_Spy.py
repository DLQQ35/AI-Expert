import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()

print(f"{Fore.CYAN} 🐍Welcome to Sentiment Spy!🐍{Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}What is your name? {Style.RESET_ALL}".strip())
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"{Fore.CYAN}Hello Agent {user_name}!")

print(f"Type a sentence and I will analyze its sentiment through my magical powers!")
print(f"Type {Fore.YELLOW}reset {Fore.CYAN}, {Fore.YELLOW}history {Fore.CYAN}or {Fore.YELLOW}exit {Fore.CYAN}to quit{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}".strip())

    if not user_input:
        print(f"{Fore.RED}Please enter a sentence to help me analyze through my magical powers.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "exit":
        print(f"{Fore.CYAN}Exiting Sentiment Spy, Farewell Agent {user_name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.YELLOW}Conversation history has been reset.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for i, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "negative":
                    color = Fore.RED
                    emoji = "😢"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f" {i}. {color}{emoji} {text}" f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😢"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}{emoji} {sentiment_type} sentiment detected." f"Polarity: {polarity:.2f}")