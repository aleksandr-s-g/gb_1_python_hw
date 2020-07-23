def fact(n):
    for el in range(1, n + 1):
        prod = 1
        for i in range(1, el + 1):
            prod = prod * i
        yield prod


for el in fact(4):
    print(el)
