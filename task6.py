def int_func(input_str):
    return input_str.capitalize()

print(int_func("text"))

input_str = input("Enter the string\n")
string_arr = input_str.split(" ")
new_str = ""
for tmp in string_arr:
    new_str = new_str + int_func(tmp) + " "
print (new_str)