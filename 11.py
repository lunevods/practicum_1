"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 11.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 08/12/2020
Дата последней модификации: 08/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 11
#версия Python: 3.9.1
"""

"""
Имеется коробка со сторонами: A × B × C.
Определить, пройдёт ли она в дверь с размерами M × K.
"""
A = int(input("Введите длину коробки:"))
B = int(input("Введите ширину коробки:"))
C = int(input("Введите высоту коробки:"))
M = int(input("Введите ширину двери:"))
X = int(input("Введите высоту двери:"))
S1=2*(A*B+B*C+A*C)
S2=M*X
if S1<=S2:
    print("Коробка пройдёт в дверь")
else:
    print("Коробка не пройдёт в дверь")
