"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 50.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 50
#версия Python: 3.9.1
"""
import random
N = random.randint(1,15)
arr = [random.randint(-100,100) for i in range(N)]
print(arr)
K = 0
T = 0
t = 0
for i in range(N):
    if arr[i] % 3 ==0:
        K += 1
print("Кол-во чисел кратных трём: " +str(K))

for i in range(N):
    if arr[i] % 2==0:
        T += arr[i]
        t += 1
A = T/t
print("Арифметическое значение: " + str(A))
arr.insert(0, K)
arr.append(A)
print(arr)
