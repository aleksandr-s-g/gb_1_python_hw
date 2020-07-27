lines = []
ru_lines = []
dict = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре"
}
try:
    with open("task3_2.txt", 'r') as f_obj:
        if not f_obj.readable():
            print("File is not readable")
            exit()
        for line in f_obj:
            print (f"line:{line}")
            ru_lines.append(line.replace(line.split(" — ")[0], dict[line.split(" — ")[0]]))
except:
    print("Some error with file!")

try:
    with open("task3_2_2.txt", 'w') as f_obj:
        if not f_obj.writable():
            print("File is not writable")
            exit()
        f_obj.writelines(ru_lines)
except:
    print("Some error with file!")
print (ru_lines)

