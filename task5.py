my_list = [7, 5, 3, 3, 2]
print(f"Исходный рейтинг {my_list}")
my_list.append(int(input("Введите число\n")))
my_list.sort(reverse=True)
print(f"Результат {my_list}")
