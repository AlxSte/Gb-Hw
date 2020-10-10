begin_dist = int(input("Введите начальную дистанцию: "))
final_dist = int(input("Введите конечную дистанцию: "))
print("День номнер 1 :", "%.2f" % begin_dist, "км.")
day = 1
while True:
    day = day + 1
    begin_dist = begin_dist + begin_dist * 0.1
    print("День номнер", day, ":", "%.2f" % begin_dist, "км.")
    if begin_dist > final_dist :
        break
print("на", day, "день спортсмен достиг результата — не менее", final_dist, "км.")