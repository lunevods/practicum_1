"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 43.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 43
#версия Python: 3.9.1
"""
import random
N = random.randint(1,15)
arr = [random.randint(-90,90) for i in range(N)]
print(arr)
arrP = []
arrN = []
for i in range(N):
    if arr[i] < 0:
        arrN.append(arr[i])
    if arr[i] > 0:
        arrP.append(arr[i])
    print (arrN)
    print (arrP)
