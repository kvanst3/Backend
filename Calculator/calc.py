import operator
from os import system
from art import logo


def calculate(ope, num1, num2):
    if ope == '+':
        return operator.add(num1, num2)
    elif ope == "-":
        return num1 - num2
    elif ope == "*":
        return operator.mul(num1, num2)
    elif ope == "/":
        return num1 / num2
    else:
        return "Invalid operator"


def calculator():
    print(logo,"\n\n")
    a = float(input("gib first num:\n"))

    with_same_num = True
    while with_same_num:
        o = input("pick operator:\n")
        b = float(input("gib next num:\n"))
        try:
            result = calculate(o, a, b)
            print(result)
        except Exception as e:
            print(type(e))
            break
        if input(f"Wanna keep calculating using {result}?['y' to continue]\n") == 'y':
            a = result
        else:
            with_same_num = False
            system('clear')
            calculator()


calculator()