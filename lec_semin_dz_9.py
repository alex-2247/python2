'''1. Напишите следующие функции:
+ Нахождение корней квадратного уравнения
+ Генерация csv файла с тремя случайными числами в каждой строке. 
100-1000 строк.
+ Декоратор, запускающий функцию нахождения корней квадратного уравнения 
с каждой тройкой чисел из csv файла.
+ Декоратор, сохраняющий переданные параметры и результаты работы функции 
в json файл.
2. Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса'''

'''Создаем отдельные функции для уравнения и для генерации .csv
Далее создаем создаем два декоратора, которые будем запускать в виде
множественного декорирования.
Чтобы схема работала, создам словарь глобальной области видимости,
буду дополнять его прогонами целевой функции, а в конце записать его в json

Похоже, не так. Надо деко-инпут сделать внешним, в нем в цикле вызывать деко-оутпут,
а в нем уже вызывать целевую функцию, а также все операции с выгрузкой в json ОДНОЙ строки.
И без всяких глобальных списков.

2,1,3      входная строка без решений
1,-4,4      входная строка с одним решением
2,5,-7      входная строка с "ровным" решением'''

import csv
import json
import time
from random import randint
from typing import Callable
from os import path

INPUT_FILE = "quadr_equ_input.csv"
OUTPUT_FILE = "quadr_equ_output.json"
EQUATION_COUNT = 5


def csv_file_gen(trinity_count:int, min_num:int, max_num:int, \
                file_name:str) -> None:
    '''- Генерация csv файла с тремя случайными числами в каждой строке.'''
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.writer(f_write, dialect='excel')
        for _ in range(trinity_count):
            num_1 = randint(min_num, max_num+1)
            num_2 = randint(min_num, max_num+1)
            num_3 = randint(min_num, max_num+1)
            csv_write.writerow([num_1, num_2, num_3])


def outer_input_deco(csv_file_name:str):
    if not path.isfile(csv_file_name):
        print("Отсутствует csv-файл входных данных, идёт создание...")
        csv_file_gen(EQUATION_COUNT, -20, 20+1, csv_file_name)
        print("...создание csv-файла входных данных завершено")
    def input_deco(func: Callable):
        def wrapper_inp(*args, **kwargs):
            # print(f'(wrapper_inp1) Запуск функции {func.__name__} в {time.time()}')
            # print('(wrapper_inp2)', csv_file_name)

            with open(csv_file_name, 'r', newline='') as f:
                csv_file = csv.reader(f)
                for line in csv_file:
                    arg_a = int(line[0])
                    arg_b = int(line[1])
                    arg_c = int(line[2])
                    # print(f'Запуск функции "{func.__name__}"')
                    result = func(arg_a, arg_b, arg_c, **kwargs)    # вот здесь её вызов
                    # print(f'Результат функции "{func.__name__}": {result};  {arg_a=};  {arg_b=};  {arg_c=}\n')

            # print(f'(wrapper_inp3) Завершение функции {func.__name__} в {time.time()}')
            return result
        # print('Возвращаем декоратор-INP')
        return wrapper_inp
    return input_deco


def outer_output_deco(json_file_name:str):
    def output_deco(func: Callable):
        def wrapper_out(*args, **kwargs):
            # print('   Старт враппера-OUT')
            # print(f'   Запускаю  {func.__name__}  из враппера-OUT')
            res = func(*args, **kwargs)

            if path.isfile(json_file_name):
                with open(json_file_name, 'r', encoding='utf-8') as f:
                    my_dict = json.load(f)
            else:
                my_dict = {}
            my_dict[f'{time.time()=}'] = (args[0], args[1], args[2], res)
            with open(json_file_name, 'w', encoding='utf-8') as f:
                json.dump(my_dict, f, indent=2, ensure_ascii=False)

            # print(f'   Результат функции "{func.__name__}": {res};  {args[0]=};  {args[1]=};  {args[2]=}')
            # print(f'   Завершение враппера-OUT')
            return res
        # print('Возвращаем декоратор-OUT')
        return wrapper_out
    return output_deco


# @deco_b     # следующим стартует опреление "более дальнего" от целевой функции декоратора
# @deco_a     # сначала стартует опреление "ближнего" к целевой функции декоратора
@outer_input_deco(INPUT_FILE)
@outer_output_deco(OUTPUT_FILE)
def quadr_equ(a:int|float=2, b:int|float=-3, c:int|float=-9) \
            -> tuple[float, float] | float|None:
    '''Квадратное уравнение'''
    # print("      ", a,b,c)
    discr = b**2 - 4*a*c
    if a == 0:
        return "wrong input"
    elif discr > 0:
        return (-b + discr**0.5) / (2 * a), (-b - discr**0.5) / (2 * a)
    elif discr == 0:
        return -b / (2 * a)
    else:
        return None


if __name__ == '__main__':
    quadr_equ()     # параметры не передаю - этим занимаются декораторы




'''Дальше примеры из лекции'''




# '''В этом примере глобальная переменная x равна 73, но при сложении внутри
# функции к значению a прибавляется 42 — значение локальной переменной x.'''
# def func(a):
#     x = 42
#     res = x + a
#     return res

# x = 73
# print(func(64))




# '''Рассмотрим простой пример функции:'''
# def add_str(a: str, b: str) -> str:
#     return a + ' ' + b

# print(add_str('Hello', 'world!'))




# '''На вход передаём две строки и возвращаем новую из двух старый и пробела
# посередине. Но функцию можно переписать иначе. Вспомним, что в Python все
# функции высшего порядка. А это значит, что их можно передавать как объекты в
# другие функции:'''
# from typing import Callable

# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
    
#     return add_two_str

# print(add_one_str('Hello')('world!'))
# '''Результат получили такой же, но код работает иначе.
# ● Функция add_one_str принимает на вход один параметр в качестве начала
# строки и возвращает локальную функцию add_two_str. Обратите внимание на
# отсутствие круглых скобок. Функцию передаём , а не вызываем.
# ● Функция add_two_str принимает вторую часть строки, соединяет её с первой
# и возвращает ответ.
# ● При вызове функций значения указывается в отдельных круглых скобках.
# Первое попадает в параметр a. Далее часть строки: add_one_str('Hello')
# возвращает функцию add_two_str и уже она вызывается и принимает
# аргумент во вторых скобках.
# Благодаря передаче одной функции другой мы можем создавать замыкания.'''




# '''Внесём небольшие правки в пример кода:'''
# from typing import Callable

# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
    
#     return add_two_str

# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')

# print(hello('world!'))
# print(hello('friend!'))
# print(bye('wonderful world!'))

# print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, \
#         {id(add_one_str) = }')
# print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
# print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')
# '''Во-первых мы не изменяли исходную функцию. Но мы создали две переменные
# hello и bye и поместили в них результат работы функции add_one_str с разными
# аргументами. Теперь мы можем вызывать новые функции и получать объединённые
# строки передавая только окончание. Первая часть строки оказалась замкнута в
# локальной области видимости. И у каждой из двух новых функций область своя и
# начало строки своё.
# А теперь посмотрите на результат работы трёх нижних строк кода. Все три
# переменные являются функциями, что очевидно. Но если функция add_one_str
# является самой собой, то функции hello и bye на самом деле являются двумя
# разными экземплярами функции add_two_str. id, т.е. адреса в оперативной памяти
# разные, а названия указывают на оригинал.'''




# '''В очередной раз внесём правки в пример кода:'''
# from typing import Callable
# def add_one_str(a: str) -> Callable[[str], str]:
#     names = []
#     def add_two_str(b: str) -> str:
#         names.append(b)
#         return a + ', ' + ', '.join(names)
#     return add_two_str

# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')

# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))
# '''Во внешнюю функцию добавлен список names. При каждом вызове внутренней
# функции в список добавляется новое значение из параметра b и возвращается
# полное содержимое списка в виде строки. У каждой из двух функций hello и bye
# оказывается свой список names. Они не связаны между собой, но каждый хранит
# список имён до конца работы программы.'''




# '''Обратите внимание, что list является
# изменяемым типом данных. Что будет, если мы перепишем код и заменим list на
# неизменяемый str?'''
# from typing import Callable

# def add_one_str(a: str) -> Callable[[str], str]:
#     text = ''

#     def add_two_str(b: str) -> str:
#         nonlocal text
#         text += ', ' + b
#         return a + text
    
#     return add_two_str

# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')

# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))
# '''Изменения способа получения строки c join для списка на конкатенацию для строки
# не принципиально. Но стоит помнить, что сложение строк более дорогая операция
# по времени и по памяти, особенно если она находится внутри цикла.
# Что более важно - неизменяемый тип данных у строки text. Без добавления строчки
# кода nonlocal text была бы получена ошибка UnboundLocalError: local variable 'text'
# referenced before assignment. Мы явно указали, что хотим обращаться к
# неизменяемому объекту для изменения его значения.
# Как можно изменить неизменяемое? Мы создаём новый объект и присваиваем ему
# старое имя. Старый объект будет удалён сборщиком мусора. А команда nonlocal
# сообщает Python, что изменения ссылки на объект должны затронуть область
# видимости за пределами функции add_two_str.
# Подведём промежуточный итог. Благодаря тому что в Python всё объект, а функции
# являются функциями высшего порядка, мы можем вкладывать во внешнюю
# функцию различные переменные и внутренние функции. Далее возвращая из
# внешней функции внутреннюю создаём замыкания.'''




# '''До этого момента наш код возвращал функции, но не принимал их. Исправим
# ситуацию на примере самописной функции нахождения факториала. Напомним, что
# факториал числа - произведение чисел от единицы до заданного числа.'''
# import time
# from typing import Callable

# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result

#     return wrapper

# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# print(f'{factorial(10) = }')
# control = main(factorial)
# print(f'{control.__name__ = }')
# print(f'{control(10) = }')
# '''● Функция main принимает на вход другую функцию. Внутри функции
# определена функция wrapper, которая возвращается функцией main.
# ● Функция wrapper принимает пару параметров *args и **kwargs. С ними вы уже
# знакомы. Подобная запись позволяет принять любое число позиционных
# аргументов и сохранить их в кортеже args, а также любое число ключевых
# аргументов с сохранением в словаре kwargs.
# Обязательной строкой внутри wrapper является result = func(*args, **kwargs).
# Переданная в качестве аргумента функция func вызывается со всеми
# аргументами, которые были переданы. Дополнительно выводим информацию
# о времени запуска, результатах и времени завершения работы функции. Не
# забываем вернуть результат работы func из wrapper.
# ● Функция factorial вычисляет факториал для заданного числа.
# ● В нижней части кода запускаем поиск факториала, проверяем
# работоспособность. Далее мы создаём функцию control в которую
# помещается wrapper с замкнутой внутри функций func — нашей функцией
# factorial. При вызове контрольной функции помимо результата поиска
# факториала получаем вывод прописанный внутри wrapper.
# Замыкание переданной в качестве аргумента функции внутри другой функции
# называется декорированием функции. В нашем примере main — декоратор,
# которым мы декорировали функцию factorial.'''




# '''В языке Python есть более элегантная возможность создания декораторов —
# синтаксический сахар. Для этого используется символ “@” слитно с именем
# декоратора. Строка кода пишется непосредственно над определением функции или
# метода.'''
# import time
# from typing import Callable

# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result

#     return wrapper

# @main
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# print(f'{factorial(10) = }')
# '''Добавили декоратор @main к функции factorial. Необходимость в присваивании
# значения новой переменной отпала. Несколько нижних строк кода из старого
# примера удалили за ненадобностью. Кроме того мы сохранили старое имя функции.
# 🔥 Важно! Функция декоратор должна быть определена в коде раньше, чем
# использована. В противном случае получим ошибку NameError
# Синтаксический сахар упрощает написание кода, но не является обязательным к
# применению. Однако в случае с передачей функции в замыкание использование
# символа @ считается нормой. Связано это с тем, что присваивание переменной
# нового значения происходит очень часто в коде. И понять создаём мы замыкание
# функции или присваиваем что-то другое сложно. Когда же речь идёт о
# присваивании через @, сразу ясно что используется декоратор'''




# '''Python позволяет использовать несколько декораторов на одной функции.
# Рассмотрим на простом примере'''
# from typing import Callable

# def deco_a(func: Callable):
#     def wrapper_a(*args, **kwargs):
#         print('Старт декоратора A')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора A')
#         return res
#     print('Возвращаем декоратор A')
#     return wrapper_a

# def deco_b(func: Callable):
#     def wrapper_b(*args, **kwargs):
#         print('Старт декоратора B')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора B')
#         return res
#     print('Возвращаем декоратор B')
#     return wrapper_b

# def deco_c(func: Callable):
#     def wrapper_c(*args, **kwargs):
#         print('Старт декоратора C')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора C')
#         return res
#     print('Возвращаем декоратор C')
#     return wrapper_c

# @deco_c
# @deco_b
# @deco_a
# def main():
#     print('Старт основной функции')

# main()
# # main()
# # main()
# '''Мы создали три одинаковых декоратора, которые сообщают о начале и завершении
# работы и о моменте декорирования: A, B, C.
# Обратите внимание на порядок декораторов у функции main. Ближайший к функции
# декоратор A. Декоратор С находится первым в списке, т.е. он максимально удалён
# от основной функции.
# При запуске кода процесс декорирования начинает снизу вверх, с A, далее B и лишь
# потом C.
# Прежде чем выполнить код основной функции запускается код верхнего
# декоратора С, далее B, в конце нижний A и только потом код функции main. После
# того как декорированная функция завершила работу и вернула результат
# декораторы завершают работу в обратном старту порядке, снизу вверх. В
# зависимости от решаемых задач порядок декорирования может привести к разным
# результатам.'''




# '''До этого мы вкладывали одну функцию в другую для создания замыкания. Если мы
# хотим передавать в декоратор дополнительные параметры, понадобится третий
# уровень вложенности. Рассмотрим пример кода.'''
# import time
# from typing import Callable

# def count(num: int = 1):
#     def deco(func: Callable):
#         def wrapper(*args, **kwargs):
#             time_for_count = []
#             result = None
#             for _ in range(num):
#                 start = time.perf_counter()
#                 result = func(*args, **kwargs)
#                 stop = time.perf_counter()
#                 time_for_count.append(stop - start)
#             print(f'Результаты замеров {time_for_count}')
#             return result
        
#         return wrapper
    
#     return deco

# @count(10)
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# print(f'{factorial(100) = }')
# print(f'{factorial(100) = }')
# '''● Внешняя функция count принимает на вход целое число num. Данный
# параметр будет использован для цикла for.
# ● Функция deco как и в прошлых примерах принимает декларируемую функцию.
# ● Внутренняя функция wrapper создаёт список time_for_count для хранения
# результатов замеров быстродействия.
# ○ Запускаем цикл for столько раз, сколько мы передали в декоратор: @count(10)
# ○ Внутри цикла for замеряем текущее время. Далее выполняем функцию
# и сохраняем результат в переменную. Замеряем время после
# окончания работы функции и сохраняем разницу в список.
# ○ После завершения цикла сообщаем результаты из списка
# time_for_count и возвращаем результат работы декларируемой функции.
# ● Используя обёртку для факториала делаем 10 замеров и смотрим время на
# вычисления.
# 🔥 Важно! Последняя строка дублируется не случайно. Каждый из двух
# запусков делает по 10 замеров. Если бы список time_for_count был создан на
# уровень выше, в функции deco, произошло бы его замыкание. В результате
# каждый новый вызов функции factorial дополнял бы уже существующий список,
# а не создавал бы новые 10 значений.
# Декоратор с параметром может принимать любые значения в зависимости от
# предназначения.
# 🔥 Важно! Для оценки быстродействия кода рекомендуется использовать
# модуль timeit из “батареек Python”, а не созданный выше декоратор.'''




# '''Рассмотрим код из прошлой главы, но добавим строку документации в функцию
# factorial.'''
# import time
# from typing import Callable

# def count(num: int = 1):
#     def deco(func: Callable):
#         def wrapper(*args, **kwargs):
#             time_for_count = []
#             result = None
#             for _ in range(num):
#                 start = time.perf_counter()
#                 result = func(*args, **kwargs)
#                 stop = time.perf_counter()
#                 time_for_count.append(stop - start)
#             print(f'Результаты замеров {time_for_count}')
#             return result
        
#         return wrapper
    
#     return deco

# @count(10)
# def factorial(n: int) -> int:
#     """Returns the factorial of the number n."""
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# print(f'{factorial(100) = }')
# print(f'{factorial.__name__ = }')   # factorial.__name__ = 'wrapper'
# help(factorial) # wrapper(*args, **kwargs)

# '''Вместо ожидаемого вывода документации о функции и её названия получаем
# информацию об обёртке wrapper:
# factorial.__name__ = 'wrapper'
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)
# Чтобы исправить ситуацию, воспользуемся декоратором wraps из functools.'''
# import time
# from typing import Callable
# from functools import wraps

# def count(num: int = 1):
#     def deco(func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             time_for_count = []
#             result = None
#             for _ in range(num):
#                 start = time.perf_counter()
#                 result = func(*args, **kwargs)
#                 stop = time.perf_counter()
#                 time_for_count.append(stop - start)
#             print(f'Результаты замеров {time_for_count}')
#             return result
        
#         return wrapper
    
#     return deco

# @count(10)
# def factorial(n: int) -> int:
#     """Returns the factorial of the number n."""
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# print(f'{factorial(100) = }')
# print(f'{factorial.__name__ = }')   # factorial.__name__ = 'factorial'
# help(factorial) # factorial(n: int) -> int Returns the factorial of the number n.
# '''Декоратор wraps добавляется к функции wrapper, т.е. к самой глубоко вложенной
# функции. В качестве аргумента wraps должен получить параметр декларируемой
# функции. Теперь factorial возвращает свои название и строку документации.'''




# '''Рассматривая возможности по замыканию переменных мы создали кэширующий
# декоратор. В модуле functools есть декоратор cache с подобным функционалом. При
# необходимости кэширования данных рекомендуется использовать именно его, как
# более оптимальное решение из коробки.'''
# from functools import cache

# @cache
# def factorial(n: int) -> int:
#     print(f'Вычисляю факториал для числа {n}')
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# print(f'{factorial(10) = }')
# print(f'{factorial(15) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
# '''Как вы видите только первые вызовы запускают функцию. Повторный вызов с уже
# передававшимся аргументом обрабатывается декоратором cache.'''




# '''этот короткий кусочек кода - трехминутная задачка из лекции'''
# import json
# a = 'Hello world!'
# b = {key: value for key, value in enumerate(a)}
# c = json.dumps(b, indent=3, separators=('; ', '= '))
# print(f'{type(b)=},   {b=}')
# print(c)




'''Дальше задачи с семинара'''




# '''Задание №1 
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.'''
# from typing import Callable

# def deco(a: int, count: int) -> Callable [[], None]:
#     def ugadai() -> None:
#         for i in range(count):
#             num = int(input('Введите число 1 - 100: '))
#             if num > a:
#                 print('Число больше')
#             elif num < a:
#                 print('Число меньше')
#             else:
#                 print('Вы угадали')
#                 break
#     return ugadai

# game = deco(20, 5)
# game()




# '''Задание №2
# Дорабатываем задачу 1.   Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.'''
# import random

# def deco(func):
#     def wrapper(a: int, count: int):
#         if a < 1 or a > 100:
#             a = random.randint(1,101)
#         if count < 1 or count > 10:
#             count = random.randint(1,11)
#         result = func(a, count)
#         return result
#     return wrapper

# @deco
# def ugadai(a: int, count: int) -> None:
#     for i in range(count):
#         num = int(input('Введите число 1 - 100: '))
#         if num > a:
#             print('Число больше')
#         elif num < a:
#             print('Число меньше')
#         else:
#             print('Вы угадали ')
#         break

# ugadai(108, 17)




# '''Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.'''
# import json
# from pathlib import Path

# def deco_file(func):
#     file = Path(f'{func.__name__}.json')#Имя файла должно совпадать с именем декорируемой функции
#     if file.is_file():
#         with open(file, 'r', encoding='utf-8') as f:
#             data = json.load(f)
#     else:
#         data =[]

#     def wrapper(*args, **kwargs):
#         new_data = {'args':args, **kwargs}#ключевой параметр сохраните как отдельный ключ json словаря
#         result = func(*args, **kwargs)
#         data.append(new_data)
#         with open(file, 'w', encoding='utf-8') as f:#'w' для json вместо 'a'
#             json.dump(data, f)
#         return result
#     return wrapper

# @deco_file
# def call(*args, **kwargs):
#     pass

# call(31,15,178, x = 18, z = 'a')




# '''Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.'''
