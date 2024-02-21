def sum(term, a, next, b):
    if a > b: return 0
    return term(a)+sum(term,next(a),next,b)

def term(x): return x 
def next(x): return x+1

while True:
    a = int(input("\nНачальное число: "))
    while True:
        b = int(input("Конечное число: "))
        if a > b:
            print("Некорректное значение границы\n")
        else:
            break
    result = sum(term, a, next, b)
    print("Итоговая сумма:", result)
    proc = input("\nПродолжить? - ")
    if proc.lower() in ('no','нет'):
        break