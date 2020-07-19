def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= a and b <= c:
        return a + c
    elif c <= a and c <= b:
        return a + b


print(my_func(1, 1, 1))
print(my_func(2, 1, 3))
print(my_func(1, 3, 5))
print(my_func(7, 1, 4))
