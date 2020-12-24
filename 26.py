"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 26.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 26
#версия Python: 3.9.1
"""

import math
A = float(input("Введите число А:"))
x = A
if x <= 0:
    fx = 0
    print("x <= 0; f(A) =:", fx)
elif 0 < x < 1:
    fx = x
    print("0 < x < 1; f(A) =:", fx)
else:
    fx = math.pow(x, 4)
    print("x >= 1; f(A) =:", fx)
