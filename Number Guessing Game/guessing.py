import random
import os
print("Welcome to the Number Guessing Game :)")
def u_input():
    num = int(input("Guess a number:"))
    return num
random_number = random.randint(1,20)
print("The computer has guessed a number!")
flag = True
while flag:
    num = u_input() 
    if num > 20 or num < 1:
        print("Not in range. Please try again!")
    elif random_number - num > 0 and random_number - num <= 2:
        print("Very close, Try greater value")
    elif random_number - num < 0 and random_number - num >= -2:
        print("Very close, Try lesser value")
    elif random_number > num:
        print("Try greater value")
    elif random_number < num:
        print("Try lesser value")
    else:
        print("Your guess is right")
        user_input = input("Do you want to continue y/n: ").lower()
        if user_input == 'y':
            os.system('cls')
            random_number = random.randint(1,20)
            print("The computer has guessed a number!")
        else:
            print("Thanks for playing")
            flag = False
input("Press return key to exit.....")