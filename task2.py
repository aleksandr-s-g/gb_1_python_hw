class MyZeroDivisionError(Exception):
    def __init__(self):
        print("you cannot divide by zero")


a = int(input("a = "))
b = int(input("b = "))
try:
    print(f"a/b = {a / b}")
except ZeroDivisionError as e:
    MyZeroDivisionError()

