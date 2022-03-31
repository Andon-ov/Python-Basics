# 1.	Реколта
# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино. От 1 кв.м
# лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.
import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())
wine = ((x * y) * 0.4) / 2.5
needed_wine = abs(z - wine)
if z > wine:
    print(f'It will be a tough winter! More {math.floor(needed_wine)} liters wine needed.')
elif z <= wine:
    print(f'Good harvest this year! Total wine: {math.floor(wine)} liters.')
    print(f'{math.ceil(needed_wine)} liters left -> {math.ceil(needed_wine / workers)} liters per person.')

# o	“{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
# 	И двата резултата трябва да са закръглени към по-високото цяло число
