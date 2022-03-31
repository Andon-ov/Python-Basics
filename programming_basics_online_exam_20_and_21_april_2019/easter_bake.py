# Задача 5. Великденски козунаци
# Един пакет захар е 950 грама, а един пакет брашно е 750 грама. Напишете програма,
# която изчислява колко пакета захар и брашно трябва да купи Деси, за да й стигнат за направата на козунаците,
# като знаете за всеки един козунак по колко грама захар и брашно са изразходени.
# Също намерете кое е най-голямото количество захар и брашно, които са използвани.
# Вход
# От конзолата се чете 1 ред:
# •	 Броят на козунаците – цяло число в интервала [1 ... 100]
# За всеки козунак се чете:
# o	Количество изразходвана захар (грамове) – цяло число в интервала [1 … 10000]
# o	Количество изразходвано брашно (грамове) – цяло число в интервала [1 … 10000]
# Изход
# Да се отпечатат на конзолата 3 реда:
import math

n = int(input())
flour = 0
sugar = 0
max_sugar = 0
max_flour = 0
for i in range(n):
    consumed_sugar = int(input())
    sugar += consumed_sugar
    if consumed_sugar > max_sugar:
        max_sugar = consumed_sugar

    consumed_flour = int(input())
    flour += consumed_flour
    if consumed_flour > max_flour:
        max_flour = consumed_flour
# Един пакет захар е 950 грама, а един пакет брашно е 750 грама

required_packages_flour = math.ceil(flour / 750)
required_packages_sugar = math.ceil(sugar / 950)
print(f"Sugar: {required_packages_sugar}")
print(f"Flour: {required_packages_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
# Пакетите захар и брашно да бъдат закръглени към най-близкото цяло число нагоре.
