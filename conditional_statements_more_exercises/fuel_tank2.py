
# Ако водача има карта за отстъпки,  той се възползва от следните намаления за литър гориво:
# 18 ст. за литър бензин, 12 ст. за литър дизел и 8 ст. за литър газ.
# Ако шофьора е заредил между 20 и 25 литра включително, той получава 8 процента отстъпка от крайната цена,
# при повече от 25 литра гориво, той получава 10 процента отстъпка от крайната цена.
# •	Бензин – 2.22 лева за един литър,  2.04
# •	Дизел – 2.33 лева за един литър 2.21
# •	Газ – 0.93 лева за литър 0.85


type_fuel = input()
fuel = float(input())
cart = input()
sum = 0

if type_fuel == "Gas" and cart == 'Yes':
    sum += fuel * 0.85
elif type_fuel == "Gas" and cart == 'No':
    sum += fuel * 0.93

if type_fuel == "Gasoline" and cart == 'Yes':
    sum += fuel * 2.04
elif type_fuel == "Gasoline" and cart == 'No':
    sum += fuel * 2.22

if type_fuel == "Diesel" and cart == 'Yes':
    sum += fuel * 2.21
elif type_fuel == "Diesel" and cart == 'No':
    sum += fuel * 2.33

if 20 < fuel <= 25:
    sum *= 0.92
elif fuel > 25:
    sum *= 0.90

print(f'{sum:.2f} lv.')

