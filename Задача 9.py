"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задача 9.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 08/12/2020
Дата последней модификации: 08/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 9
#версия Python: 3.9.1
"""

"""
Дано натуральное число. Определить, будет ли это число: нечётным, кратным 7.
"""
import random
n= random.randint(1, 100)
print("Число:", n)
if n%2==1:
    print("Нечётное")
else:
    print("Чётное")
if n%7==0:
    print("Кратно 7")
else:
    print("Не кратно 7")
