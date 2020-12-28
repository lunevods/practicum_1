"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 40.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 40
#версия Python: 3.9.1
"""

import random
N = int(input("Количество элементов массива:"))
A = [random.randint(-10,10) for i in range(0, N)]
print(A)
for i in range(N):
    if A[i] < 0:
        A[i] = A[i]**2
print(A)
