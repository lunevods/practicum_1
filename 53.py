"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 53.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 53
#версия Python: 3.9.1
"""
M = int(input("Введите количество строк: "))
x = []
for i in range(0, M):
    print("Введите строку:",  end=' ')
    x.append(input())
def count(y):
    a = 0
    b = 0
    i = 0
    while i < len(y):
        z = y[i]
        if z.lower() in ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']:
            a += 1
        else:
            b += 1

        i += 1
    return a, b
for y in x:
    a, b = count(y)
    print("В строке %s %s гласных и %s согласных " % (y, a, b))
