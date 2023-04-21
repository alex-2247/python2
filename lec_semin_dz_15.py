'''Практическое (домашнее) задание (предположительное, из презентации)
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.'''

'''Задание сделаю в майские каникулы.
Сейчас высылаю, чтобы опрокинуть дедлайн'''





















# # KIRILL 22:15
# import logging

# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.ERROR, filename='ZeroDivisionError.log', encoding='utf-8',
#                     format=FORMAT, style="{")
# logger = logging.getLogger(__name__)


# def func_div_two(a, b) -> float:
#     try:
#         res = a / b
#     except ZeroDivisionError as e:
#         logger.error(f'Ошибка деления числа {a} на число {b}')
#         return float('inf')
#     return res

# if __name__ == '__main__':
#     print(func_div_two(8, 0))





# Владимир Николаев 22:20
# def deco_file(func):
#     file = Path(f'{func.__name__}.json')
#     if file.is_file():
#         with open(file, 'r', encoding='utf-8') as f:
#             data = json.load(f)
#     else:
#         data = []
#     def wrapper(*args, **kwargs):
#         new_data = {'args': args, **kwargs}
#         result = func(*args, **kwargs)
#         data.append(new_data)
#         with open(file, 'w', encoding='utf-8') as f1:
#             json.dump(data, f1)
#         return result
#     return wrapper

# @deco_file
# def call(*args, **kwargs):
#     pass


# # call(12, 24, 56, ax = 12, b = 45)
# '''"""№3
# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
# """'''



# alexa 22:42
# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.INFO, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\15\\deco1.log', encoding='utf-8',format=FORMAT, style="{")
# logger = logging.getLogger(__name__)

# def deco_file(func):
#     data = []
#     def wrapper(*args, **kwargs):
        
#         new_data = {'args': args, **kwargs}
#         result = func(*args, **kwargs)
#         data.append(new_data)
#         # print(new_data)
#         logger.info(new_data)
#         return result
#     return wrapper

# @deco_file
# def call(*args, **kwargs):
#     pass

# call(12, 24, 56, ax = 12, b = 45)




# '''Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.'''
# alexa 22:53
# FORMAT = '{levelname} - {asctime} : {msg}'
# logging.basicConfig(level=logging.INFO, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\15\\deco1.log', encoding='utf-8', format=FORMAT, style="{")
# logger = logging.getLogger(__name__)

# def deco_file(func):
#     data = []
#     def wrapper(*args, **kwargs):
        
#         new_data = {'args': args, **kwargs}
#         result = func(*args, **kwargs)
#         data.append(new_data)
#         # print(new_data)
#         logger.info(f' {func.__name__}{new_data}')
#         return result
#     return wrapper

# @deco_file
# def call(*args, **kwargs):
#     pass

# call(12, 24, 56, ax = 12, b = 45)



# '''Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.'''
# import datetime
# print(datetime.strptime(date_text, 'Дата %d %B %Y. День
# недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))
# alexa 23:54
# from datetime import datetime
# from calendar import monthrange

# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.ERROR, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\15\\data_text.log', encoding='utf-8',
#                     format=FORMAT, style="{")
# logger = logging.getLogger(__name__)

# MONTH = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя','дек')
# DAY = ("пон", "вто", "сре", "чет", "пят", "суб","вос")


# def data_text(text: str) -> datetime:
#     try:
#         count, day, month = text.split()
#     except ValueError as e:
#         logger.error(f'Ошибка введения даты')
#         return None
#     count = int(count[:-2])
#     day = DAY.index(day[:3])
#     month = MONTH.index(month[:3]) + 1
#     year = datetime.now().year
#     count_days = monthrange(year, month)[1]
#     # print(count_days)
#     count_week = 0
#     for d in range(1, count_days+1):
#         date = datetime(day= d, month= month, year= year)
#         if date.weekday() == day:
#             # print(date)
#             count_week += 1
#             if count == count_week:
#                 return date

# print(data_text('3-я среда мая'))
