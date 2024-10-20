import random

emojis = { "r" : "🪨" , "s" : "✂️" , "p" : "📃" }
choices =( "r" , "s" , "p" )

def get_user_input():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Number!")

def display_choice(user_choice,computer_choice):
     print(f'You chose {emojis[user_choice]}')
     print(f'Computer chose {emojis[computer_choice]}')
     

def determine_winer(user_choice,computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif(
        (user_choice =='r' and computer_choice == 's') or
        (user_choice =='s' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You Win')
    else:
        print('You Lose')

def play_game():                
    while True:
        user_choice = get_user_input()
        computer_choice = random.choice(choices)

        display_choice(user_choice,computer_choice)

        determine_winer(user_choice,computer_choice)

        should_continue = input("Continue?(y/n):").lower()
        if should_continue == 'n':
            break
play_game()


