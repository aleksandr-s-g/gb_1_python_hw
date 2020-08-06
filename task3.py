class NaNException(Exception):
    def __init__(self):
        print("Sorry, it is not number")

list = []
while True:
    n = input()
    if n == "stop":
        break
    if n.isdigit():
        list.append(int(n))
    else:
        NaNException()

print (list)