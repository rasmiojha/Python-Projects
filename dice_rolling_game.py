import random

while True:
    choice=input("Roll The dice?(y/n):").lower()
    if choice == 'y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(dice1,dice2)
    elif choice == 'n':
        print("Thanks for Playinyg!")
        break
    else:
        print("Invalid Choice!")

#Loop
    #Ask.roll.the.dice?
    #If user enters Y
        #Generate two random numbers
        #Print them
    #If user enters n
        #Print thank you message 
        #Terminate
    #Else
        #Print Invalid Choice
