"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 22.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 22
#версия Python: 3.9.1
"""

A = float(input("Введите вещественное число A:"))
B = float(input("Введите вещественное число B:"))
C = float(input("Введите вещественное число C:"))

if A < B and B > C:
    print("Оба неравенства выполняются:")
if A < B:
    print("Выполняется неравенство А < B:")
if B > C:
    print("Выполняется неравенство B > C:")