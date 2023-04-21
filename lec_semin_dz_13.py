'''Практическое (домашнее) задание (предположительное, из презентации)
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины.'''

'''Задание сделаю в майские каникулы.
Сейчас высылаю, чтобы опрокинуть дедлайн'''


















# '''Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.'''
# def get_num(text: str = None) -> int:
#     # num = 1
    
#     while True:
#         num_str = input(text)
#         try:
#             num = int(num_str)
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
#             try:
#                 num = float(num_str)
#                 break
#             except ValueError as e:
#                 print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
#     return num

# number = get_num('Введите число: ')
# print(f'Введено число {number}')




# '''Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.'''
# def my_get(my_dict, my_key, my_def):
#     result = None
#     try:
#         result = my_dict[my_key]
#     except KeyError as e:
#         print(f'Такой ключ не найден, возвращаю дефаулт')
        
# print(my_get({'one':1, 'two':2, 'three':3}, 'two', 'оппа...'))
# print(my_get({'one':1, 'two':2, 'three':3}, 'four', 'оппа...'))




# '''Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.'''
# class UserException(Exception):
#     pass


# class LevelError(UserException):
#     # pass
#     def __str__():
#         print('ошибка уровня')


# class AccessError(UserException):
#     # pass
#     def __str__():
#         print('ошибка доступа')




# '''Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.'''
# import json


# class User:
#     def __init__(self, name :str, id: int, level: int):
#         self.name = name
#         self.id = id
#         self.level = level
   
# def reed_json(file_name: str):
#     users = set()
#     with open(file_name, 'r', encoding='utf-8') as f:
#         data = json.load(f)
    
#     for level, value in data.items():
#         for id, name in value.items():
#             users.add(User(name = name,id= int(id),level= int(level)))
#     return users
      
# print(reed_json('ident.json'))




# '''Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.'''
# import json
# from user_exception import LevelException, AccesException

# class User:
#     def __init__(self, name :str, id: int, level: int):
#         self.name = name
#         self.id = id
#         self.level = level
    
#     def __eq__(self, other) -> bool:
#         return self.id == other.id and self.name == other.name

# class Project:
#     def __init__(self) -> None:
#         self.users = set()
#         self.user = None

#     def reed_json(self, file_name: str):
        
#         with open(file_name, 'r', encoding='utf-8') as f:
#             data = json.load(f)
        
#         for level, value in data.items():
#             for id, name in value.items():
#                 self.users.add(User(name = name,id= int(id),level= int(level)))
#         return self.users

# # print(reed_json('ident.json'))
#     def enter(self, name: str, id: int):
#         u1 = User(name= name, id= id, level= 0)
        
#         if u1 not in self.users:
#             raise AccesException
        
#         for item in self.users:
#             if u1 == item:
#                 self.user = item
#                 return self.user

#     def add_user():
#         pass


# class BaseException(Exception):
#     pass

# class LevelException(BaseException):
#     print('Level')

# class AccesException(BaseException):
#     print('Access')
