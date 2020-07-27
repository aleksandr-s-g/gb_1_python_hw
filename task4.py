import random
numbers = []
try:
    with open("task4.txt", 'w') as f_obj:
        if not f_obj.writable():
            print("File is not writable")
            exit()
        line = ''
        for i in range(0,100):
            line = line + str(random.randrange(0, 100500)) + " "
        f_obj.write(line)
except:
    print("Some error with file!")

try:
    with open("task4.txt", 'r') as f_obj:
        if not f_obj.readable():
            print("File is not readable")
            exit()
        numbers = f_obj.readline().split(" ")
except:
    print("Some error with file!")
arr_sum = 0
for num in numbers:
    if not num == '':
        arr_sum = arr_sum + int(num)
print(f"sum: {arr_sum}")
