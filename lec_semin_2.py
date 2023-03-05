import math
print(math.pi, math.e, math.inf, math.nan, math.tau, sep="\n")
print(dir(math))
print(help(math.gcd))








# my_text = input('Введите что-нибудь: ')
# if my_text.isdecimal():
#     print("Введено целое число " + str(int(my_text)))
#     print(bin(int(my_text)), oct(int(my_text)), hex(int(my_text)))
# elif my_text.isascii():
#     print("Введен ASCII-текст")
# else:
#     print("Введено что-то другое")







# my_text = input("Введи любой текст: ")
# print(type(my_text), id(my_text), hash(my_text))

# help()







# import math
# import decimal

# decimal.getcontext().prec=42
# diametr = decimal.Decimal(input("Введите диаметр: "))
# pi = decimal.Decimal(math.pi)

# MIN_LIMIT = 0
# MAX_LIMIT = 1000

# if diametr <= MAX_LIMIT:
#     length = pi * diametr
#     square = pi * (diametr/2)**2
#     print(length, square)
# else:
#     print("Введенный диаметр слишком большой")
