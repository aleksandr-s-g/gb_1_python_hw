a = int(input("Введите a\n"))
b = int(input("Введите b\n"))
cur = a
i = 1
while True:
    print (i, "-й день: ", round(cur,2))
    if cur > b:
        break
    cur= cur * 1.1
    i+=1

print("Ответ: на ",i,"-й день спортсмен достиг результата — не менее ",b,"км.")