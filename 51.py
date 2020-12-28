"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 51.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 51
#версия Python: 3.9.1
"""
M = int(input("Введите количество строк: "))
x = []
for i in range(0, M):
    print("Введите строку:",  end=' ')
    x.append(input())
maxx= 0
for y in x:
    d = len(y)
    if d > maxx:
        maxx = d
print("Максимальная длина строки:", maxx)
for y in x:
    d = len(y)
    if d < maxx:
        for i in range(0, maxx - d):
            y = '*' + y
    print(y)
