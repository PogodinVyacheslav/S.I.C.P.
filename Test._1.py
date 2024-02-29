from fractions import Fraction

def generate_pairs(a, b, n):
    for i in range(n):
        yield (a+i*4, b+i*4)

def func3(func1, func2, pairs):
    result = Fraction(0)
    for a, b in pairs:
        fraction = Fraction(1, func1(a, b))
        if func2 == '+':
            result += fraction
        elif func2 == '-':
            result -= fraction
        elif func2 == '*':
            result *= fraction
        elif func2 == '/':
            result /= fraction
    return float(result)

def func4():
    while True:
        a = int(input("\nНачальное значение: "))
        b = int(input("Конечное значение: "))
        n = int(input("Количество пар: "))
        func2 = input("Знаки ряда: ")
        
        pairs = generate_pairs(a, b, n)
        result = func3(lambda a, b: a + b, func2, pairs)
        print("\nРезультат:", round(result, 6))
        
        proc = input("\nПродолжить? - ")
        if proc.lower() in ('no','нет'):
            break
func4()





