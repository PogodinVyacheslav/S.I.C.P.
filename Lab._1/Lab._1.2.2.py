def sum(term, a, next, b):
    def iter(a, result):
        if a > b:
            return result
        else:
            return iter(next(a), result + term(a))
    return iter(a, 0)

def identity(i):
    return i
def increment(i):
    return i+1

while True:
    a = int(input("\nНачальное число: "))
    while True:
        b = int(input("Конечное число: "))
        if a > b:
            print("Некорректное значение границы\n")
        else:
            break
    result = sum(identity, a, increment, b)
    print("Итоговая сумма:", result)
    proc = input("\nПродолжить? - ")
    if proc.lower() in ('no','нет'):
        break


