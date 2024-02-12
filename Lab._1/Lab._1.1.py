def square(x, i):
    result = []
    for _ in range(i):
        x **= 2
        result.append(x)
    return result

while True:
    num = int(input("\nЧисло алгоритма: "))
    while True:
        i = int(input("Кол-во лог. шагов: "))
        if i <= 0:
            print("Необходимо положительное число\n")
        else:
            break
    result = square(num, i)
    print("Послед. возведение:", result)
    proc = input("\nПродолжить? - ")
    if proc.lower() in ('no','нет'):
        break