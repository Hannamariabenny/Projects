import os
exit_flag = False

def getInstructions():
    os.system('cls')
    print("Operations we have in this 'Simple Calculator'\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

def getNumbers(op):
    list1 = []
    count = 1
    getNumber_flag = False
    if op == '/':
        div_count_flag = False
        while div_count_flag == False:
            try:
                value1 = int(input("Enter your value 1: "))
                value2 = int(input("Enter your value 2: "))
            except ValueError:
                print("Invalid Value")
            else:
                div_count_flag = True
        return value1, value2
   
    else:
        while getNumber_flag == False:
            u_input = str(input(f"Enter your value {count}: "))
            if u_input == 'done':
                getNumber_flag = True
                return list1
            else:
                u_input_flag = False
                try:
                    u_input = int(u_input)
                except ValueError:
                    u_input_flag = True
                if u_input_flag:
                    print("Invalid Value")
                else:
                    list1.append(int(u_input))
                    count += 1

def Add(op):
    print("Addition\nEnter 'done' when you want to get the result")
    a = getNumbers(op)
    sum = 0
    for i in a:
        sum += i
    print(f"Sum is {sum}")
    
def Sub(op):
    print("Subtraction\nEnter 'done' when you want to get the result")
    a = getNumbers(op)
    diff = a[0]
    for i in range(1, len(a)):
        diff -= a[i]
    print(f"Difference is {diff}")

def Mul(op):
    print("Multiplication\nEnter 'done' when you want to get the result")
    a = getNumbers(op)
    prod = 1
    for i in a:
        prod *= i
    print(f"Product is {prod}")
    
def Div(op):
    print("Division\nEnter 'done' when you want to get the result")
    num1, num2 = getNumbers(op)
    if num2 == 0:
            print("Division is not possible")
    else:
            print(f"Quotient is {num1 / num2}") 

def Options(op):
    if op == 'options':
        option = getInstructions()
    elif op == '+' or op =='add' or op == 'addition':
        os.system('cls')
        Add('+')
    elif op == '-' or op == 'sub' or op == 'subtraction':
        os.system('cls')
        Sub('-')
    elif op == '*' or op == 'mul' or op == 'multiplication':
        os.system('cls')
        Mul('*')
    elif op == '/' or op == 'div' or op == 'division':
        os.system('cls')
        Div('/') 
    else:
        print("Operation not found")

def startingFunction():
    print("SIMPLE CALCULATOR - Type 'options'")
    op = str(input("What operation do you want to perform?\n")).lower()
    Options(op)

while exit_flag == False:
    a = startingFunction()
    u_input = str(input("Press 'Enter' to go back or enter 'Exit' to exit: ")).lower()
    if u_input == 'exit':
        exit_flag = True
    else:
        os.system('cls')
