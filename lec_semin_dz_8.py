'''Решить задачи, которые не успели решить на семинаре.
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.'''
import os
import json


'''Для выгрузки в сериализацию создаём ОДНОУРОВНЕВЫЙ словарь:
key = полный путь + '\\' + имя папки/файла
value = список ['file'|'dir', Размер]
Требование условий "Для дочерних объектов указывайте родительскую директорию"
реализовано тем, что родительская директория прописана в ключе объекта,
прямо перед его (папки/файла) именем.'''
def os_walk(dir_arg:str) -> None:
    path_dict = {}
    for dir_path, dir_list, file_list in os.walk(dir_arg):
        print(f'  {dir_path = }\n  {dir_list = }\n  {file_list = }\n')
        for item in file_list:  # обход по списку файлов в текущей папке
            file_name = dir_path+'\\'+item
            file_size = os.path.getsize(file_name)
            path_dict[file_name] = ['file', file_size]
        for item in dir_list:  # обход по списку директорий в текущей папке
            dir_name = dir_path+'\\'+item
            path_dict[dir_name] = ['dir', 0]
        # print(path_dict)
        # print('\n')

    # Займемся вычислением размера файлов в папках
    for key, val in path_dict.items():
        path_list = key.split('\\')
        if val[0]=='dir' and val[1]==0:
            dir_name = path_list[len(path_list)-1]
            sum_bytes = 0
            # print(f'{key}   {dir_name=}')
            for key2, val2 in path_dict.items():
                path_list = key2.split('\\')
                if path_list[len(path_list)-2] == dir_name:
                    sum_bytes += val2[1]
            # print(sum_bytes)
            path_dict[key] = ['dir', sum_bytes]

    # Зальем наш словарь в json
    with open('my_path.json', 'w', encoding='utf-8') as f:
        json.dump(path_dict, f, ensure_ascii=False, indent=2)


my_dir = os.getcwd() + '\package6'      # папка которую будем обходить
print(f'{my_dir = }')
os_walk(my_dir)
