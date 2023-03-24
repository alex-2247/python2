'''Напишите функцию принимающую на вход только ключевые параметры и 
возвращающую словарь, где ключ - значение переданного аргумента, а значение - 
имя аргумента. Если ключ не хешируем, используйте его строковое представление.'''


def trans_dict(**kwargs):
    '''создает "перевернутый" словарь аргументов, 
    где ключ - это значение, а значение - имя аргумента'''
    dict2 = {}
    for key in kwargs:
        value = kwargs[key]
        if str(type(value)) in \
                    ("<class 'list'>", "<class 'set'>", "<class 'dict'>"):
            value = hash_convert(value)
        dict2[value] = key
    return dict2


def hash_convert(serial):
    '''Преобразует нехешируемые коллекции в строку'''
    result = ""
    if str(type(serial)) == "<class 'dict'>":
        for key, value in serial.items():
            result += str(key) + str(value)
    else:
        for item in serial:
            result += str(item)
    return result


def print_dict(dictin):
    '''Функция печати словаря в терминал'''
    for key, value in dictin.items():
        print(f'{key=},    {value=}')


# Проверим работу наших функций
dict_2 = trans_dict(one=2, two=3.14, three="qwerty", four=True\
                    , five=False, six=[0,1,1,2,3,5,8,13], seven={1,2,3,4,5}\
                    , eight={'one':42, 'two':3.14, 'ten':'Hello world!'})
print("Итоговый словарь: ", dict_2, "\n")
print("Итоговый словарь по элементу в строке:")
print_dict(dict_2)


