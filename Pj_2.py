initial_sec = input("Введите число секунд: ")
result_hour = int(initial_sec) // 3600
result_min =(int(initial_sec) % 3600) // 60
result_sec = int(initial_sec) % 60
print("%02d:%02d:%02d" % (result_hour, result_min, result_sec))


