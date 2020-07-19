tmp_sum = 0;
global_sum = 0;
final_flag = False
while not final_flag:
    tmp_sum = 0
    input_str = input(
        "введите последовательность чисел, разделенных через пробел, "
        "для завершение вместо числа введите /\n")
    input_arr = input_str.split(" ")
    for i in input_arr:
        if i.isdigit():
            tmp_sum = tmp_sum + float(i)
        elif i == "/":
            final_flag = True
            break
    global_sum = global_sum + tmp_sum
    print("Сумма этого ввода ", tmp_sum)
    print("Общая сумма ", global_sum)

print("Финальная сумма равна ", global_sum)
