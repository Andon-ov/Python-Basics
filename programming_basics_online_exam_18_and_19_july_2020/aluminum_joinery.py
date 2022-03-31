# Алуминиева дограма
# Фирма-производител на алуминиева дограма приема поръчки за изработката и монтаж със следния ценоразпис за един брой.
# Фирмата приема само поръчки на едро (над 10 бр.). В зависимост от поръчания брой дограми,
# фирмата прави различна отстъпка на своите клиенти.
# Фирмата предлага също и доставка на поръчките си срещу 60 лв.
# Размер	Единична цена	Отстъпка от цената
# 90X130	110 лв.	 Над 30 броя – 5%
#  Над 60 броя – 8%
# 100X150	140 лв.	 Над 40 броя – 6%
#    Над 80 броя – 10%
# 130X180	190 лв.	 Над 20 броя – 7%
#    Над 50 броя – 12%
# 200X300	250 лв.	 Над 25 броя – 9%
#    Над 50 броя – 14%
#
#
# Ако поръчката надвишава 99 броя  – върху крайната цена се начисляват допълнителни 4% отстъпка
# (след като се начисли цената за доставка, ако има такава).
# При поръчка под 10 бр. на конзолата да бъде изписано "Invalid order"
# Вход:
# Потребителят въвежда 3 реда:
# 1.	Брой дограми – цяло число в интервала [0..1000];
# 2.	Вид на дограмите – текст "90X130" или "100X150" или "130X180" или "200X300";
# 3.	Начин на получаване – текст
# •	С доставка - "With delivery"
# •	Без доставка - "Without delivery"
# Изход:
# Извежда се едно число – стойността на поръчката, в следния формат:
# o	"{Обща стойност на поръчката} BGN"
# Резултатът да се форматира до втори знак след десетичната запетая.
number_of_windows = int(input())
type_of_windows = input()
shipment_method = input()
price = 0
sum = 0

if type_of_windows == '90X130' and number_of_windows > 10:
    price = 110
    if 30 < number_of_windows < 59:
        price *= 0.95
    elif number_of_windows > 60:
        price *= 0.92
elif type_of_windows == '100X150' and number_of_windows > 10:
    price = 140
    if 40 < number_of_windows < 79:
        price *= 0.94
    elif number_of_windows > 80:
        price *= 0.90
elif type_of_windows == '130X180' and number_of_windows > 10:
    price = 190
    if 20 < number_of_windows < 49:
        price *= 0.93
    elif number_of_windows > 50:
        price *= 0.88
elif type_of_windows == '200X300' and number_of_windows > 10:
    price = 250
    if 25 < number_of_windows < 49:
        price *= 0.91
    elif number_of_windows > 50:
        price *= 0.86
sum = number_of_windows * price

if shipment_method == "With delivery" and number_of_windows > 10:
    sum += 60
if number_of_windows > 99:
    sum *= 0.96
if number_of_windows > 10:
    print(f'{sum:.2f} BGN')
elif number_of_windows < 10:
    print(f'Invalid order')
# Ако поръчката надвишава 99 броя  – върху крайната цена се начисляват допълнителни 4% отстъпка
# (след като се начисли цената за доставка, ако има такава).
# При поръчка под 10 бр. на конзолата да бъде изписано "Invalid order"

