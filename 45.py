"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 45.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 45
#версия Python: 3.9.1
"""
import random
N = int(input("Введите количество элементов массива: "))
A = [random.randint(-100, 100) for i in range(N)]
print(A)
n = []
p = []
for i in range(N):
    if A[i] > 0:
        p.append(A[i])
    else:
        n.append(A[i])
sumn=abs(sum(n))
sump=sum(p)
Q=(sumn-sump)
print("Сумма элементов с положительными значениями: ", sumn)
print("Сумма элементов с отрицательными значениями: ", sump)
print("Разница:", Q)
if sumn == sump:
    print("Сумма отрицательных и положительных элементов массива равна")
if sumn > sump:
    A.append([Q])
if sump > sumn:
    A.append([Q])
print(A)
