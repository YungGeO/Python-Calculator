import math


class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y


name = str = input("enter your name ")
print(f"hello {name} ")

action = str = input("you want to do add,sub,mul or exit? \n ").lower()


while (action != "exit"):

    if action in ["add", "sub", "mul"]:

        x = int(input("give me first number "))
        y = int(input("give me second number "))
        calc = Calculator(x, y)
        if action == "add":
            print(f"Result {calc.add()}\n")
        elif action == "sub":
            print(f"Result: {calc.sub()}\n")
        elif action == "mul":
            print(f"Result: {calc.sub()}\n")
    else:
        print("unknown command.Try again")
    action = input("you want to do add,sub,mul or exit?").lower()


print("\nexiting program...")
