"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 31.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 31
#версия Python: 3.9.1
"""

from random import randint
N = 20
arr = [randint(0, 100) for i in range(N)]
print(arr)
for i in range(N-1):  
    for m in range(N-1-i):
        if arr[m] > arr[m+1]:
            temp = arr[m]
            arr[m] = arr[m+1]
            arr[m+1] = temp
print(arr)            
