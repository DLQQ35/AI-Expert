import random
from colorama import init, Fore, Style
init(autoreset = True)

def game():
    def player_choice():
        move_choice = input(Fore.GREEN + "Choose your symbol (R/P/S): " + Style.RESET_ALL).upper()
        while move_choice not in ['R', 'P', 'S']:
            move_choice = input(Fore.GREEN + "Choose your symbol (R/P/S): " + Style.RESET_ALL).upper()
            if move_choice == 'R':
                return ('You have chosen rock.')
            elif move_choice == 'P':
              return ('You have chosen paper.')
            elif move_choice == 'S':
                return ('You have chosen scissors.')

    def ai_choice():
        ai_move = random.choice(['R', 'P', 'S'])
        if ai_move == 'R':
            print(Fore.BLUE + "AI has chosen rock." + Style.RESET_ALL)
        elif ai_move == 'P':
            print(Fore.BLUE + "AI has chosen paper." + Style.RESET_ALL)
        elif ai_move == 'S':
            print(Fore.BLUE + "AI has chosen scissors." + Style.RESET_ALL)

    def rock_paper_scissors(player_choice, ai_choice):
        print("Welcome to the game of Rock, Paper and Scissors!")
        if player_choice == ai_choice:
            print(Fore.RED + "It's a tie!" + Style.RESET_ALL)

        elif (player_choice == 'R' and ai_choice == 'S') or (player_choice == 'P' and ai_choice == 'R') or (player_choice == 'S' and ai_choice == 'P'):
            print(Fore.RED + "You win!" + Style.RESET_ALL)
    
        else:
            print(Fore.RED + "AI wins!" + Style.RESET_ALL)

        print("Do you want to play again? (Y/N)")
        if input().upper() == 'Y':
            game()
        else:
            print("Thanks for playing!")

    if __name__ == "__main__":
        rock_paper_scissors()