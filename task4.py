def my_func(x, y):
    print (x ** y)
    if x > 0 and y < 0:
        z = 1
        for i in range (0, -y):
            z = z * x
        print (1/z)


my_func(1, -2)
print("__________")
my_func(2, -2)
print("__________")
my_func(2.3, -5)
print("__________")
my_func(7.6, -20)