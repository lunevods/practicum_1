"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 25.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 25
#версия Python: 3.9.1
"""

a = float(input("Введите число А:"))
x = a
if x <= 2:
    fx = x**2 + 4*x + 5
    print("x <= 2; f(a) =:", fx)
else:
    fx = 1 / (x**2 + 4*x + 5)
    print("x > 2; f(a) =:", fx)
