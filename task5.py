income = int(input("Введите доходы\n"))
expenses = int(input("Введите расходы\n"))

if income > expenses:
    print("Фирма работает в прибыль")
    print("Прибыль составляет:", income - expenses)
elif income == expenses:
    print ("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")