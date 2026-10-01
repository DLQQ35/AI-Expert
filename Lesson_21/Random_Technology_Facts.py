import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_facts():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did You Know?: {fact_data['text']}")
    else:
        print("Failed to fetch fact")

while True:
    user_input = input("Press Enter to get a random fact or type 'q' or 'exit' to quit: ")
    if user_input.lower() in ['q', 'exit']:
        print("Goodbye!")
        break
    get_random_facts()