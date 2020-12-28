"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 61.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 61
#версия Python: 3.9.1
"""
import re
list_numbers = []
sum = 0
sum_count = 0
multiply = 1
multiply_sum = 0
i = 1
while True:
    print("Введите число:", end=' ')
    string = re.sub(r'\D', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа ")
        continue
    number = int(string)
    list_numbers.append(number)
    if i % 2 != 0:
        sum += number
        sum_count += 1
    else:
        multiply = multiply * number
        multiply_sum += 1

    i += 1
    if list_numbers[len(list_numbers) - 1] == 55555:
        break
    
print("Сумма:", sum)
print("Количество слагаемых:", sum_count)

print("Произведение", multiply)
print("Количество множителей:", multiply_sum)
