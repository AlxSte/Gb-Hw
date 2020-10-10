proceeds = int(input("Введите выручку"))
costs = int(input("Введите издержки"))
if proceeds > costs:
    print ("Фирма отработала с прибылью. Рентабельность выручки: ≈", int(((proceeds-costs)/proceeds)*100), "%")
    person = int(input("Введите количество сотрудников"))
    print("Прибыль на одного человека ровна ", (proceeds-costs)/person)
elif proceeds < costs:
    print ("Фирма отработала в убыток.")
else:
    print ("Фирма отработала в 0.")1
    