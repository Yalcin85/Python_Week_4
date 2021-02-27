import add, subtract, multiply, divide, time
print("Welcome to Calculator")
while True:

    print("press + for addition ")
    print("press - for subtraction ")
    print("press * for multiplication ")
    print("press / for division ")
    print("Press E for exit")
    print("---------------------")
    print("Please select operation: ")
    operator = input()

    if operator == '+':
        add.add()

    elif operator == '-':
        subtract.subtract()

    elif operator == '*':
        multiply.multiply()

    elif operator == '/':
        divide.divide()

    elif operator == 'E' or operator == "e":
        print("Thanks for using the calculator")
        time.sleep(3)
        break

    else:
        print("Error, try again. \n")
