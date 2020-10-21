def my_func(x, y):
    x_begin = x
    for el in range(abs(y)-1):
        x = x * x_begin
    return 1/x

x = int(input("x "))
y = int(input("y "))
print(my_func(x, y))

