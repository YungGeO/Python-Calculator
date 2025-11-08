import math


class Calculator():
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y


name = str = input("enter your name ")
print(f"hello {name} ")

action = str = input("you want to do add,sub,mul or exit?").lower()
calc = Calculator()

while (action != "exit"):

    if action == "add":
        X = int(input("give me first number "))
        Y = int(input("give me second number "))
        calc.add(X, Y)
    elif action == "sub":
        X = int(input("give me first number "))
        Y = int(input("give me second number "))
        calc.sub(X, Y)
    elif action == "mul":
        X = int(input("give me first number "))
        Y = int(input("give me second number "))
        calc.mul(X, Y)
    else:
        print("unknown command.Try again")
    action = input("you want to do add,sub,mul or exit?").lower()
