number = input("введите натуральное число. Каждая цифра станет элементом массива\n")
test_list = []
for c in number:
    test_list.append(int(c))
print(f"Ваш массив:{test_list}")

for i in range (0,len(test_list)-1, 2):
    test_list[i],test_list[i+1] = test_list[i+1], test_list[i]

print(f"Ваш массив после обмена:{test_list}")