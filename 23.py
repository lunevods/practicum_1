"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 23.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 23
#версия Python: 3.9.1
"""

import math
x = float(input("Введите вещественное число x:"))
y = float(input("Введите вещественное число y:"))
if x > y:
    z = math.sqrt(x * y)
    print(z)
else:
    z = math.log(x + y, math.e)
    print(z)
