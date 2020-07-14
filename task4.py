input_str = input("Введите строку\n")
str_arr = input_str.split(" ")
for i in range(0, len(str_arr)):
    print(str_arr[i][:10])
print(str_arr)
