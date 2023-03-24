'''Напишите функцию для транспонирования матрицы'''


def trans_matrix(matr_1):
    '''Сначала, создаем целевую матрицу с размерностью повёрнутой исходной.
    Затем, заполняем целевую матрицу элементами исходной, во вложенных циклах'''
    matr_2 = [0] * len(matr_1[0])
    for i in range(len(matr_1[0])):
        matr_2[i] = [0] * len(matr_1)
    for i in range(len(matr_1)):
        for j in range(len(matr_1[0])):
            matr_2[j][i] = matr_1[i][j]
    return matr_2


def print_matrix(matrix):
    '''Функция печати матрицы в терминал'''
    for i in range(len(matrix)):
        print(matrix[i])


# Создаём исходную матрицу
original_matrix = [[11,12,13,14], [21,22,23,24], [31,32,33,34]]

print('Исходная матрица:')
print_matrix(original_matrix)
print('\n'+'Транспонированная матрица:')
print_matrix(trans_matrix(original_matrix))
