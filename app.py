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

    def div(self):
        if self.y == 0:
            return "invalid number try again"
        return self.x/self.y

    def sqrt(self):
        if self.x < 0:
            return "cant find the sqrt of a negative number"
        return math.sqrt(self.x)


name = input("enter your name ")
print(f"hello {name} ")

action = input("you want to do add,sub,mul,div,sqrt or exit? \n ").lower()


while (action != "exit"):

    if action in ["add", "sub", "mul", "div", "sqrt"]:
        if (action == "sqrt"):
            x = int(input("give me the number "))
            calc = Calculator(x, 0)
            print(f"Result:  {calc.sqrt()}")
        else:
            x = float(input("give me first number "))
            y = float(input("give me second number "))
            calc = Calculator(x, y)
            if action == "add":
                print(f"Result {calc.add()}\n")
            elif action == "sub":
                print(f"Result: {calc.sub()}\n")
            elif action == "mul":
                print(f"Result: {calc.mul()}\n")
            elif action == "div":
                print(f"Result: {calc.div()}\n")
    else:
        print("unknown command.Try again")
    action = input("you want to do add,sub,mul,div,sqrt or exit?").lower()


print("\nexiting program...")
