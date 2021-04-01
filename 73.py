"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 73.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/03/2021
Дата последней модификации: 10/03/2021
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 73
#версия Python: 3.9.1
"""
import random

N = 4
M = 6


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


def get_average(row):
    sum = 0
    for element in row:
        sum += element

    return sum/len(row)


def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1

    return column


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

sum = 0

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        sum += A[i][j]
        j += 1

    i += 1

i = 0

while i < len(A):
    j = 0

    sum_row = 0
    while j < len(A[i]):
        sum_row += A[i][j]
        j += 1

    A[i].append(sum_row/sum)

    i += 1

print("Сумма всех элементов:", sum)
print("Модифицированная матрица:")
print_matrix(A)
