number = int(input("Введите целое положительное число"))
max = 0
while (number // 10) > 0:
    if number % 10 > max:
        max = number % 10
    number = number // 10
print("Самая большая цифра в числе", max)
