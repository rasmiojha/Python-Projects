#Generate a random number
import random

number_to_guess = random.randint(1,100)
while True:
    try:
        user_input = int(input("Guess the number between 1 and 100:"))
        
        if user_input<number_to_guess:
            print("Too Low!")
        elif user_input>number_to_guess:
            print("Too High!")
        else:
            print("Congratulation! You have guessed the Number.",number_to_guess)
            break
    except ValueError:    
        print("Please Enter a valid Number")



#Loop
    #Ask the user to make a guess
    #If not a valid number
        #print an error 
    #If number<guess
        #print too low
    #if number>guess
        #print too high
    #else
        #print well done