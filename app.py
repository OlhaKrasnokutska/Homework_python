number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

operator_ = input('Enter operator "+", "-", "*" or "/": ')

def add(num1, num2):
    print(num1 + num2)

def subt(num1, num2):
    print(num1 - num2)

def mult(num1, num2):
    print(num1 * num2)

def div(num1, num2):
    print(num1 / num2)

def calc(num1, num2, operator):
    if operator == "+":
        add(num1, num2)
    elif operator == "-":
        subt(num1, num2)
    elif operator == "*":
        mult(num1, num2)
    elif operator == "/":
        div(num1, num2)
    else:
        print("Choose correct operator")


calc(number1, number2, operator_)