import random

ROCK = 'R'
PAPER = 'P'
SCISSORS = 'S'
emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📄'}
choices = tuple(emojis.keys())
computer_win = 0
player_win = 0


def get_user_choice():
    while True:
        player_choice = input("Rock, paper, scissors? (R/P/S): ").upper()
        if player_choice in choices:
            return player_choice
        else:
            print("Invalid choice, please select 'R', 'P', or 'S'.")


def display_choices(player_choice, computer_choice):
    print(f'You chose {emojis[player_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def checking_round(player_choice, computer_choice, player_win, computer_win):
    if player_choice == computer_choice:
        print('Draw')
    elif (
            (player_choice == ROCK and computer_choice == SCISSORS) or
            (player_choice == SCISSORS and computer_choice == PAPER) or
            (player_choice == PAPER and computer_choice == ROCK)):
        print('You win this round!')
        player_win += 1
    else:
        print('You lose this round!')
        computer_win += 1
    print(f"Score - You: {player_win}, Computer: {computer_win}")
    return player_win, computer_win


def checking_winner(player_win, computer_win):
    if player_win == 3:
        print("Congratulations! You have won the whole tournament!")
        return True
    elif computer_win == 3:
        print("Sorry, you lost the tournament!")
        return True
    return False


def play_game():
    player_win = 0
    computer_win = 0

    while True:
        player_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(player_choice, computer_choice)

        player_win, computer_win = checking_round(player_choice, computer_choice, player_win, computer_win)

        if checking_winner(player_win, computer_win):
            break


play_game()

