input_str = input("Введите число\n")

num = int(input_str[0])
i = 1
max_num = num
while i < len(input_str):
    num = int(input_str[i])
    if num > max_num:
        max_num = num
    i += 1
print(max_num)
