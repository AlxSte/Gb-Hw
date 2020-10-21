"""Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def personal_information(fname, lname, dateb, city, email, phone):
    return [f"{fname} {lname} {dateb} {city} {email} {phone}"]

fname = input("Введите имя: ")
lname = input("Фамилию: ")
dateb = input("Дату рождения: ")
cit  = input("Город: ")
email = input("email: ")
phone = input("Телефон: ")
res = personal_information(fname=fname, lname=lname, dateb=dateb, city=cit, email=email, phone=phone)
print(res)