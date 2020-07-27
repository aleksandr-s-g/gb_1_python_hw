lines = []
try:
    with open("task2.txt", 'r') as f_obj:
        if not f_obj.readable():
            print("File is not readable")
            exit()
        lines = f_obj.readlines()
except:
    print("Some error with file!")

print(f"Num of lines:{len(lines)}")
for i in range(0, len(lines)):
    print(f"There is {len(lines[i].split(' '))} words in {i + 1} line")
