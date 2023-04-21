'''Практическое (домашнее) задание (предположительное, из презентации)
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.'''

'''Задание сделаю в майские каникулы.
Сейчас высылаю, чтобы опрокинуть дедлайн'''


















# '''Создадим класс, экземпляры которого можно вызывать. Например для 
# добавления очередного элемента во внутренний словарь класса по типам.'''
# from collections import defaultdict

# class Storage:
#     def __init__(self):
#         self.storage = defaultdict(list)

#     def __str__(self):
#         txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
#         return f'Объекты хранилища по типам:\n{txt}'

#     def __call__(self, value):
#         self.storage[type(value)].append(value)
#         return f'К типу {type(value)} добавлен {value}'

# s = Storage()
# print(s(42))
# print(s(72))
# print(s('Hello world!'))
# print(s(0))
# print(s(3.14))
# print(s(2.72))
# print(s)

# '''При создании класса используется продвинутая версия словаря из модуля 
# collections — defaultdict. Словарю передана функция list. При обращении к 
# несуществующему ключу вместо ошибки будет создан ключ и вызвана функция list 
# для создания значения ключа.

# Каждый вызов экземпляра добавляет переданный аргумент value в словарь storage 
# и возвращает строку с информацией о выполненном действии. Последовательно 
# вызывая экземпляр с числами и текстом выводим его на печать и видим содержимое 
# на момент печати.

# Плюсом вызова экземпляра является то, что он не удаляется из памяти после 
# вызова как обычная функция. Следовательно экземпляр может накапливать 
# значения, использоваться в технологии мемоизации. Её рассматривали на лекции 
# о декораторах.'''




# '''Задание Перед вами несколько строк кода. Напишите что выведет программа, 
# не запуская код. У вас 3 минуты.'''
# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __repr__(self):
#         return f'MyClass(a={self.a}, b={self.b})'
    
#     def __call__(self, *args, **kwargs):
#         self.a.append(args)
#         self.b.update(kwargs)
#         return True

# x = MyClass([42], {73: True})
# y = x(3.14, 100, 500, start=1)
# x(y=y)
# print(x)




# '''Задание №1
# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений. Параметр k передаётся при 
# создании экземпляра. Добавьте метод для просмотра ранее вызываемых значений 
# и их факториалов.'''
# '''2! = 2
#    3! = 6
#    4! = 24
#    5! = 96'''
# class Factorial:
#     def __init__(self, k: int):
#         self.k = k 
#         self.val_list = [None]* self.k
#         self.key_list = [None]* self.k  

#     def __call__(self, n: int, *args, **kwds):
#         if(n==1 or n==0):
#             return 1
#         result = 1
#         for i in range(1, n + 1):
#             result = i * result
#         self.val_list.append(result)
#         self.val_list.pop(0)
#         self.key_list.append(n)
#         self.key_list.pop(0)
#         # print(self.val_list, self.key_list)
#         return result
    
#     def view(self):
#         return f'{self.val_list} \n {self.key_list}'
    
# f = Factorial(5)
# print(f(6))
# print(f(7))
# print(f(8))
# print(f(5))
# print(f(4))
# print(f(3))
# print(f.view())




# '''Доработаем задачу 1. 
# Создайте менеджер контекста, который при выходе сохраняет значения 
# в JSON файл.'''
# class Factorial:
#     def __init__(self, k: int):
#         self.k = k 
#         self.val_list = [None]* self.k
#         self.key_list = [None]* self.k  

#     def __call__(self, n: int, *args, **kwds):
#         if(n==1 or n==0):
#             return 1
#         result = 1
#         for i in range(1, n + 1):
#             result = i * result
#         self.val_list.append(result)
#         self.val_list.pop(0)
#         self.key_list.append(n)
#         self.key_list.pop(0)
#         # print(self.val_list, self.key_list)
#         return result
    
#     def view(self):
#         return f'{self.val_list} \n {self.key_list}'
    
#     def __enter__(self):
#         pass

#     def __exit__(self):
#         pass


    
# f = Factorial(5)
# print(f(6))
# print(f(7))
# print(f(8))
# print(f(5))
# print(f(4))
# print(f(3))
# print(f.view())



# def __enter__(self):
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         with open('file_factorial.json', 'w', encoding='utf-8') as f:
#             slovar = dict(zip(self.key_list, self.val_list ))
#             json.dump(slovar, f, ensure_ascii=False, indent=2)
            

    
# # f = Factorial(5)
# with Factorial(5) as f:

#     print(f(6))
#     print(f(7))
#     print(f(8))
#     print(f(5))
#     print(f(4))
#     print(f(3))
#     print(f.view())





# '''Создайте класс-генератор. 
# Экземпляр класса должен генерировать факториал числа в диапазоне 
# от start до stop с шагом step. 
# Если переданы два параметра, считаем step=1. 
# Если передан один параметр, также считаем start=1.'''
# class MyFac:
#     # def __init__(self, start:int=None, stop:int=None, step:int=None) -> None:
#     #     if step==None:
#     #         self.step = 1
#     #     else:
#     #         self.step = step

#     #     if stop==None:
#     #         self.start = 1
#     #         self.stop = start
#     #     else:
#     #         self.start = step
#     #         self.stop = stop
#     def __init__(self, *args):
#         match len(args):
#             case 1:
#                 self.start = 1
#                 self.stop = args[0]
#                 self.step = 1
#             case 2:
#                 self.start = args[0]
#                 self.stop = args[1]
#                 self.step = 1
#             case 3:
#                 self.start = args[0]
#                 self.stop = args[1]
#                 self.step = args[2]

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         # if(self.start==1 or self.stop==0):
#         #      return 1
#         while self.start < self.stop:
#             result = 1
#             for i in range(2, self.start+1):
#                 result = i * result
#             self.start += self.step
#             return result
#         raise StopIteration
    
# fib = MyFac(0, 8, 1)
# for num in fib:
#     print(num)

# # print(fib.__next__())
# # print(fib.__next__())
# # print(fib.__next__())
# # print(fib.__next__())
