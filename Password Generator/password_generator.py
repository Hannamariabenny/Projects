import random
import os
characters = {
    'upper':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
             'U', 'V', 'W', 'X', 'Y', 'Z'],
    'lower':['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z'],
    'numbers':['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    'symbols':['!', '@', '#', '%', '^', '*', '.']
}
categories = ['upper', 'lower', 'numbers', 'symbols']
flag = True
print("Password Generator!")
while flag:
    password = ''
    for i in range(0,9):
        c_random = random.randint(0,3) 
        u_random = random.randint(0,25) 
        n_random = random.randint(0,9) 
        s_random = random.randint(0,6) 
        if len(characters[categories[c_random]]) == 26:
            password += (characters[categories[c_random]][u_random])
        elif len(characters[categories[c_random]]) == 10:
            password += (characters[categories[c_random]][n_random])
        else:
            password += (characters[categories[c_random]][s_random])
    print(f'Your generated password is "{password}"')
    if input("Do you want to regenerate (y/n)?: ").lower() == 'y':
        os.system('cls')
    else:
        input("Press return key to exit...")
        flag = False