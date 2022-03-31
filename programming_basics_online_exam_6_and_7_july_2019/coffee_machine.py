# Задача 3. Кафемашина


#  При избрана напитка без захар има 35% отстъпка.
#  При избрана напитка "Espresso" и закупени поне 5 броя, има 25% отстъпка.
#  При сума надвишава 15 лева, 20% отстъпка от крайната цена,
# Отстъпките се прилагат в реда на тяхното описване.


drink = input()
sugar = input()
number_of_drinks = int(input())
sum = 0

if drink == "Cappuccino":
    if sugar == 'Without':
        sum += number_of_drinks * 1
    elif sugar == 'Normal':
        sum += number_of_drinks * 1.20
    elif sugar == 'Extra':
        sum += number_of_drinks * 1.60
elif drink == "Espresso":
    if sugar == 'Without':
        sum += number_of_drinks * 0.90
    elif sugar == 'Normal':
        sum += number_of_drinks * 1
    elif sugar == 'Extra':
        sum += number_of_drinks * 1.20
elif drink == "Tea":
    if sugar == 'Without':
        sum += number_of_drinks * 0.50
    elif sugar == 'Normal':
        sum += number_of_drinks * 0.60
    elif sugar == 'Extra':
        sum += number_of_drinks * 0.70
if sugar == 'Without':
    sum *= 0.65
if drink == 'Espresso' and number_of_drinks >=5:
    sum *= 0.75
if sum > 15:
    sum *= 0.80

print(f'You bought {number_of_drinks} cups of {drink} for {sum:.2f} lv.')









# Изход
# На конзолата трябва да се отпечата един ред:
# "You bought {брой напитки} cups of {напитка} for {крайна цена} lv."
# Цената да бъде форматирана до втората цифра след десетичния знак.