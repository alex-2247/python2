def func_1():
    '''Напишите функцию, которая принимает на вход строку - абсолютный путь до 
    файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, 
    расширение файла.'''    

    path_tuple = split_path("C:\dir1\dir2\dir3\dir4\\file.ext")
    print(f'{type(path_tuple)=};\n{path_tuple=}')


def split_path(my_path:str) -> tuple:
    list_path = my_path.split("\\")
    # print(list_path)
    only_path = ""
    for i, item in enumerate(list_path):
        if (i+1) == len(list_path):
            only_name = item.split('.')[0]
            only_ext = item.split('.')[1]
            break
        # print(len(list_path), i, item)
        only_path += item + "\\"

    # print(only_path, only_name, only_ext)
    return only_path, only_name, only_ext


def func_2():
    '''Напишите однострочный генератор словаря, который принимает на вход три 
    списка одинаковой длины: имена str, ставка int, премия str с указанием 
    процентов вида «10.25%». В результате получаем словарь с именем в качестве 
    ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка 
    умноженная на процент премии'''

    names = ["Иван", "Николай", "Пётр"]
    salaries = [125_000, 96_000, 109_000]
    awards = ["10.1%", "25.2%", "13.3%"]

    award_dict = {name: salary*float(award.replace("%",""))/100 for name, salary, award in zip(names, salaries, awards)}
    # print(float("10.25%".replace("%",""))/100)

    # Проверим как работает наш генератор
    award_iter = iter(award_dict.items())
    print(f'{type(award_iter)=};   {award_iter=}')
    for item in award_iter:
        print(item)


def func_3():
    '''Создайте функцию генератор чисел Фибоначчи (см. Википедию)'''
    my_count = 12   # проверим функцию на 12-и итерациях
    fibo_iter = iter(fibo_gen(my_count))
    for i, num in enumerate(fibo_iter, start=1):
        print(f'шаг {i}: число Фибоначчи = {num}')


def fibo_gen(arg:int):
    '''1  2  3  4  5  6  7   8   9  10  11  12
       0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89'''
    pre_last_num = last_num = 0
    for step in range(1, arg+1):
        if step == 2:
            pre_last_num = 1
        number = pre_last_num + last_num
        # print(f'{i=}   {pre_last_num=}   {last_num=}   {number=}')
        pre_last_num = last_num
        last_num = number
        yield number


print(f'Задача 1:   {func_1.__doc__}\n')
print(f'Задача 2:   {func_2.__doc__}\n')
print(f'Задача 3:   {func_3.__doc__}\n')
my_choice = int(input("Введите номер задачи:"))

if my_choice == 1:
    func_1()
elif my_choice == 2:
    func_2()
else:
    func_3()
