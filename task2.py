input_sec = int(input("Введите время в секундах\n"))
sec = input_sec % 60
min = (int((input_sec - sec) / 60)) % 60
hour = (int((input_sec - min - sec) / (60 * 60)))

print('{:02}'.format(hour), ":", '{:02}'.format(min), ":", '{:02}'.format(sec))
