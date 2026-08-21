import random
from colorama import init, Fore, Style

init(autoreset=True)

def player_choice():
    move_choice = input(Fore.GREEN + "Choose your symbol (R/P/S): " + Style.RESET_ALL).upper()
    while move_choice not in ['R', 'P', 'S']:
        move_choice = input(Fore.GREEN + "Choose your symbol (R/P/S): " + Style.RESET_ALL).upper()
    return move_choice

def ai_choice():
    ai_move = random.choice(['R', 'P', 'S'])
    if ai_move == 'R':
        print(Fore.BLUE + "AI has chosen rock." + Style.RESET_ALL)
    elif ai_move == 'P':
        print(Fore.BLUE + "AI has chosen paper." + Style.RESET_ALL)
    elif ai_move == 'S':
        print(Fore.BLUE + "AI has chosen scissors." + Style.RESET_ALL)
    return ai_move

def rock_paper_scissors():
    print("Welcome to the game of Rock, Paper and Scissors!")
    p_choice = player_choice()
    a_choice = ai_choice()
    
    if p_choice == a_choice:
        print(Fore.RED + "It's a tie!" + Style.RESET_ALL)
    elif (p_choice == 'R' and a_choice == 'S') or \
         (p_choice == 'P' and a_choice == 'R') or \
         (p_choice == 'S' and a_choice == 'P'):
        print(Fore.RED + "You win!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "AI wins!" + Style.RESET_ALL)
        
    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == 'Y':
        rock_paper_scissors()
    else:
        print("Thanks for playing!")

if __name__ == '__main__':
    rock_paper_scissors()