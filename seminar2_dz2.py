""" Погружение в Python (семинары)
Урок 2. Простые типы данных
1. Напишите программу, которая получает целое число и возвращает его 
шестнадцатеричное строковое представление. Функцию hex используйте для 
проверки своего результата.
2. Напишите программу, которая принимает две строки вида “a/b” - дробь с 
числителем и знаменателем. Программа должна возвращать сумму и произведение* 
дробей. Для проверки своего кода используйте модуль fractions. Необязательное 
задание     """

# Задача 2 (строковые дроби)

# from fractions import Fraction
import fractions

frac1  = input('Введи первую дробь в формате “a/b”: ')
frac2  = input('Введи вторую дробь в формате “a/b”: ')
# frac1  = "1/3"
# frac2  = "3/5"

numerator1 = int(frac1[:frac1.find("/")])
denominatot1 = int(frac1[frac1.find("/")+1:])
numerator2 = int(frac2[:frac2.find("/")])
denominatot2 = int(frac2[frac2.find("/")+1:])

str_sum = str(numerator1 * denominatot2 + numerator2 * denominatot1) + "/" \
        + str(denominatot1 * denominatot2)
str_mul = str(numerator1 * numerator2) + "/" + str(denominatot1 * denominatot2)
print("Сумма =", str_sum)
print("Произведение =", str_mul)

etalon_sum = fractions.Fraction(frac1) + fractions.Fraction(frac2)
etalon_mul = fractions.Fraction(frac1) * fractions.Fraction(frac2)
if etalon_sum == fractions.Fraction(str_sum) and etalon_mul == fractions.Fraction(str_mul):
	print("Fraction-проверка пройдена, мы молодцы!")
else:
	print("Что-то пошло не так")



""" код из лекции, для примера, дополненный
f1 = fractions.Fraction(1, 3)
print(f1)   # 1/3
f2 = fractions.Fraction(3, 5)
print(f2)   # 3/5
print(f1 * f2)  # 1/5
print(f1 + f2)  # 14/15
print(fractions.Fraction(1, 5) == fractions.Fraction(3, 15))    # True """
