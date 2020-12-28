"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 36.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 36
#версия Python: 3.9.1
"""

import array
import random
N = int(input("Введите количество элементов массива:"))
M = int(input("Количесвто элементов в группе:"))
K = int(input("Позиция K:"))
A = [random.randint(0, 100) for i in range(0, N)]
B = [random.randint(0, 100) for b in range(0, M)]
print(A)
print(B)
A.insert(K, B)
print(A)
