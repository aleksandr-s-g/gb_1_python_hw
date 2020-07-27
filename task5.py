def extract_numbers(str):
    numbers = []
    new_str = ''
    for c in str:
        if c.isdigit() or c == ' ':
            new_str = new_str + c
    for num in new_str.split(' '):
        if num.isdigit():
            numbers.append(int(num))
    return numbers


lines = []
dict = {}
try:
    with open("task5.txt", 'r') as f_obj:
        if not f_obj.readable():
            print("File is not readable")
            exit()
        lines = f_obj.readlines()
except:
    print("Some error with file!")

for line in lines:
    dict[line.split(':')[0]] = sum(extract_numbers(line))
print(dict)
