import requests
import random
import html
from inputimeout import inputimeout, TimeoutOccurred

EDUCATION_CATEGORY_ID = 9

API_URL = f"https://opentdb.com/api.php?amount=5&category={EDUCATION_CATEGORY_ID}&type=multiple"

def get_education_questions():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']
    return None

def run_quiz():
    questions = get_education_questions()
    if not questions:
        print("Failed to fetch trivia questions. Please try again later.")
        return

    score = 0
    for i, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(a) for a in q['incorrect_answers']]
        options = incorrects + [correct]
        random.shuffle(options)

        print(f"\nQuestion {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        while True:
                try:
                    answer = inputimeout(prompt="\nYour answer (1-4): ",timeout=10)
                    choice = int(answer)
                    if 1 <= choice <= 4:
                        break
                    else:
                       print("Invalid input! Please enter 1-4")
                except ValueError:
                    print("Invalid input! Please enter 1-4")
                except TimeoutOccurred:
                    print("\n⏰ Time's up!")
                    choice = None
                    break
        if choice is None:
            print(f"The correct answer was: {correct}\n")
        elif options[choice - 1] == correct:
                print("Correct!\n")
                score += 1
        else:
                print(f"Wrong! The correct answer was: {correct}\n")
    print(f"Final score: {score}/{len(questions)}")
    print(f"Percentage: {score / len(questions) * 100:.1f}%")

if __name__ == "__main__":
    print("Welcome to the Education Trivia Quiz!")
    run_quiz()