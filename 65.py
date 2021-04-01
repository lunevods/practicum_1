"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 65.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/03/2021
Дата последней модификации: 10/03/2021
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 65
#версия Python: 3.9.1
"""
import re
list_numbers = []

B = 5
sum = 0

while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue
    number = int(string)
    list_numbers.append(number)

    if number < 0:
        break

    if number % B == 0:
        sum += number

print("Сумма:", sum)
