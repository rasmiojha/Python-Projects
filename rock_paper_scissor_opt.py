import random
ROCK = 'r'
SCISSOR = 's'
PAPER = 'p'

emojis = {ROCK : "🪨", SCISSOR :  "✂️" , PAPER : "📃"}
choices = tuple(emojis.keys())

def get_user_input():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/s/p): ").lower()
        for user_choice in choices:
            return user_choice
        else:
            print('Invalid Choice!')

def display_choice(user_choice,computer_choice):
     print(f'You chose {emojis[user_choice]}')
     print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif(
        (user_choice == ROCK and computer_choice == SCISSOR ) or
        (user_choice == SCISSOR and computer_choice == PAPER ) or
        (user_choice ==  PAPER and computer_choice ==  ROCK )):
        print('You Win')
    else:
        print('You Lose')

def play_game():
    while True:
        user_choice = get_user_input()
        computer_choice = random.choice(choices)
        display_choice(user_choice,computer_choice)
        determine_winner(user_choice,computer_choice)
        should_continue = input('do you want to continue?(y/n)').lower()
        if should_continue == 'n':
            break
play_game()

