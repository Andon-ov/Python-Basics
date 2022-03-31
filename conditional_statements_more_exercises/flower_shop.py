# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци.
import math

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
price_of_the_gift = float(input())

magnolias = number_of_magnolias * 3.25
hyacinths = number_of_hyacinths * 4
roses = number_of_roses * 3.5
cacti = number_of_cacti * 8
sum = (magnolias + hyacinths + roses + cacti) * 0.95
needed_money = abs(price_of_the_gift - sum)
# Ако парите СА стигнали
if price_of_the_gift <= sum:
    print(f'She is left with {math.floor(needed_money)} leva.')
# Ако парите НЕ достигат:
else:
    print(f'She will have to borrow {math.ceil(needed_money)} leva.')


