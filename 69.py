"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 69.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/03/2021
Дата последней модификации: 10/03/2021
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 69
#версия Python: 3.9.1
"""
import random

N = 4  # строк
M = 5  # столбцов

def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def listsum(list):
    sum = 0
    for element in list:
        sum += element

    return sum


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)

tmp = list(zip(*A))

max_sum = 0
index_column_max_sum = 0

i = 0
while i < len(tmp):
    column = tmp[i]
    current_list_sum = listsum(column)
    if current_list_sum > max_sum:
        max_sum = current_list_sum
        index_column_max_sum = i

    i += 1

print("Матрица:")
print_matrix(A)
print("Cтолбец для которого сумма абсолютных значений элементов максимальна:",
      index_column_max_sum)
print("Наименьший элемент этого столбца:", min(tmp[index_column_max_sum]))
