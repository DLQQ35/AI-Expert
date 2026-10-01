import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/today?language=en"

def get_todays_facts():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did You Know?: {fact_data['text']}")
    else:
        print("Failed to fetch fact")

user_input = input("Press Enter to get today's fact or type 'q' or 'exit' to quit: ")
get_todays_facts()