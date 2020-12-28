"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 48.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 48
#версия Python: 3.9.1
"""
import random
N = random.randint(1,25)
arr=[random.randint(-1,1) for i in range(N)]
print(arr)
for i in range(N):
    if arr[i] ==0:
     t = arr[i-1] + arr[i-2]
     arr[i] = t
print(arr)
