"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 1.py
Автор: 2020 © Д.Л Иоффе, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: min,max
Описание: Решение задачи №№ 1
#версия Python: 3.6
"""

""

str = "28/10/2020"
print("Вот дата по-русски -",str)

date = str.split("/")
en_date = date[2]+"-"+date[1]+"-"+date[0]

print("Вот что получилось -",en_date)
