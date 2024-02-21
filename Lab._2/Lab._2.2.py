def cube(x): return x * x * x
def inc(n): return n + 1
def sum_cubes(a, b):
    return sum(map(cube, range(a, inc(b))))

while True:
    a = int(input("\nНачальное число: "))
    while True:
        b = int(input("Конечное число: "))
        if a > b:
            print("Некорректное значение границы\n")
        else:
            break
    result = sum_cubes(a, b)
    print("Сумма кубов:", result)
    proc = input("\nПродолжить? - ")
    if proc.lower() in ('no','нет'):
        break