__all__ = ['group_rename', 'create_test_dir']

from pathlib import Path
from random import choice, sample
from shutil import rmtree
import os


def group_rename(pack_name:str, want_name:str, cyfer_cnt:int, source_ext:str, target_ext:str, pos_range:tuple):
    '''Групповое переименование файлов
    
    :param pack_name: имя тестового каталога
    :param want_name: желаемое имя 
    :param cyfer_cnt: количество цифр в порядковом номере
    :param source_ext: расширение исходного файла
    :param target_ext: расширение конечного файла
    :param pos_range: диапазон позиций символов, сохраняемых из оригинального имени
    '''
    file_cnt = 0
    for item in os.listdir(pack_name):
        file_name = pack_name + '\\' + item
        if file_name[-3:] == source_ext:
            file_cnt += 1
            new_file = file_name[-12+pos_range[0]-1:-12+pos_range[1]] # срез диапазона
            new_file += want_name # желаемое имя
            new_file += ('0'*cyfer_cnt+str(file_cnt))[-cyfer_cnt:] # счетчик файлов
            new_file += '.' + target_ext # желаемое расширение
            new_file = pack_name + '\\' + new_file
            print(file_name, '  -->  ', new_file)
            os.rename(file_name, new_file)


def create_test_dir(test_dir:str, ext_lst:list[str], file_cnt:int):
    if test_dir in os.listdir():
        rmtree(test_dir)
    Path(test_dir).mkdir()

    for i in range(file_cnt):
        file_name = test_dir+'\\'
        for item in sample('qwertyuiopasdfghjklzxcvbnm1234567890', 8):
            file_name += item
        file_name += '.' + choice(ext_lst)
        with open(file_name, 'a', encoding='utf-8') as f:
            pass
    # print('qwerty', test_dir, ext_lst, file_cnt, file_name)
