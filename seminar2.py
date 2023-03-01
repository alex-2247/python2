import math
import decimal

decimal.getcontext().prec=42
diametr = decimal.Decimal(input("Введите диаметр: "))
pi = decimal.Decimal(math.pi)

MIN_LIMIT = 0
MAX_LIMIT = 1000

if diametr <= MAX_LIMIT:
    length = pi * diametr
    square = pi * (diametr/2)**2
    print(length, square)
else:
    print("Введенный диаметр слишком большой")
