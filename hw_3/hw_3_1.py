"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division_numb (numb1, numb2):
    if int(numb2) == 0:
        return "Деление на 0"
    res = int(numb1)/int(numb2)
    return res

dev1 = input("Введите число 1 ")
dev2 = input("Введите число 2 ")
division_res = division_numb(dev1, dev2)
print(division_res)