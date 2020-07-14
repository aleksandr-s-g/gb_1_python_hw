param_names = ("название", "цена", "количество", "ед.")
continue_flag = True
products = []
while continue_flag:
    print("Начинаем ввод нового товара")
    product = {}
    for param_name in param_names:
        param = input(f"Введите {param_name} ")
        product[param_name] = param
    product_iteam = (len(products) + 1, product)
    products.append(product_iteam)
    continue_flag_str = ""
    while continue_flag_str != "да" and continue_flag_str != "нет":
        continue_flag_str = input("Ввести еще один товар? да/нет ")
    if continue_flag_str == "да":
        continue_flag = True
    else:
        continue_flag = False

print(products)
statistics_dict = {}
for param_name in param_names:
    statistics_dict[param_name] = []
    for product in products:
        statistics_dict[param_name].append(product[1][param_name])
    statistics_dict[param_name] = list(dict.fromkeys(statistics_dict[param_name]))
print(statistics_dict)
