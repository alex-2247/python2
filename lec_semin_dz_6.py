'''В этом блоке практическое (домашнее) задание.
Ниже закомментированная работа с семинара'''

from package6.mystery import one_myst
from package6.mystery import myst_serial
from package6.date_check import dchk


print(f'Задача 1:   {one_myst.__doc__}\n')
print(f'Задача 2:   {myst_serial.__doc__}\n')
print(f'Задача 3:   {dchk.__doc__} \n' \
      '    (реализована в виде проверки тестового набора)')
my_choice = int(input("\nВведите номер задачи:  "))


if my_choice == 1:
    print(one_myst('Зимой и летом одним цветом', \
                   ['Елка', 'Ель', 'Елочка'], 3))
elif my_choice == 2:
    myst_serial()
else:
    print("01.01.0001", "  ", dchk("01.01.0001"))
    print("24.02.2022", "  ", dchk("24.02.2022"))
    print("29.02.2020", "  ", dchk("29.02.2020"))   # Високосный
    print("29.02.2023", "  ", dchk("29.02.2023"))   # Не високосный
    print("32.13.0000", "  ", dchk("32.13.0000"))




'''Дальше задачи и прочее с семинара'''




# '''Мой вопрос в начале семинара'''
# import sys

# print(sys)
# print(sys.builtin_module_names)
# print(*sys.path, sep='\n')

# from random import *

# print(random)
# print(random.__dir__)




# '''Задание 1
# Вспомните какие модули вы уже проходили на курсе. Создайте файл, в котором вы 
# импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).'''
# from random import randint as r_int
# from random import uniform as r_float
# from random import choice as r_sequence
# from random import shuffle as r_shuf




# from sys import argv
# import random as rnd

# '''Задание 2
# Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: 
# нижнюю и верхнюю границу и количество попыток. Внутри генерируется случайное 
# число в указанных границах и пользователь должен угадать его за заданное 
# число попыток. Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.'''
# def guess(down:int = 0, up:int = 100, chanse:int = 5) -> bool:
#     number = rnd.randint(down, up)

#     for i in range(chanse):
#         print(f"Enter number from {down} to {up} ")
#         num = int(input())
#         if num > number:
#             print(" Number is smaller ")
#         elif num < number:
#             print(" Number is bigger ")
#         else:
#             return True
#     return False      

# if __name__ == '__main__':
#     down = int(input('Enter first number: '))
#     up = int(input('Enter second number: '))
#     chanse = int(input('Enter third number: '))
#     print(guess(down, up, chanse))




# '''Улучшаем задачу 2. 
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке 
# терминала. Строка должна принимать от 1 до 3 аргументов: параметры вызова 
# функции. Для преобразования строковых аргументов командной строки в числовые 
# параметры используйте генераторное выражение.'''
# def guess(down:int = 0, up:int = 100, chanse:int = 5) -> bool:
#     number = rnd.randint(down, up)

#     for i in range(chanse):
#         print(f"Enter number from {down} to {up} ")
#         num = int(input())
#         if num > number:
#             print(" Number is smaller ")
#         elif num < number:
#             print(" Number is bigger ")
#         else:
#             return True
#     return False      

# if __name__ == '__main__':
#     # tmp_path - 1ый обязательный элемент вывода из argv, но нам он не нужен
#     tmp_path, *params = argv    
#     # down = int(input('Enter first number: '))
#     # up = int(input('Enter second number: '))
#     # chanse = int(input('Enter third number: '))
#     # print(guess(down, up, chanse))
#     print(guess(*(int(n) for n in params))) # генераторное выражение из params

# # python task2.py 2 10 3   # запустить эту строку прямо здесь в терминале VSC




# '''Задание 4
# Создайте модуль с функцией внутри. Функция получает на вход загадку, список 
# с возможными вариантами отгадок и количество попыток на угадывание. Программа 
# возвращает номер попытки, с которой была отгадана загадка или ноль, если 
# попытки исчерпаны.'''
# def mystery(m:str, answer:list, chanse: int) -> int:
#     print(m)
#     for i in range(chanse):
#         ans = input(' Введите ответ ')
#         if ans in answer:
#             return i + 1
#     return 0

# if __name__ == '__main__':
#     m = 'Зимой и летом одним цветом! '
#     an = ['Елка', 'Ель', 'Елочка']
#     ch = 5
#     print(mystery(m, an, ch))
