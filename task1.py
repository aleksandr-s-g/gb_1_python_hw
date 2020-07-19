def my_division(a, b):
    try:
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("Zero Division Error")


my_division(1, 0)
