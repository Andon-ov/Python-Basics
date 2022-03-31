# 4.Кола под наем
# Напишете програма, която спрямо даден бюджет и сезон да пресмята цената, типа и класа на кола под наем.
# Сезоните са лято и зима – "Summer" и "Winter". Типа коли са кабрио и джип – "Cabrio" и "Jeep".


#Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
budget = float(input())
# •	Втори ред –  Сезон – текст "Summer" или "Winter"
season = str(input())
# •	При бюджет по-малък или равен от 100лв.:
 # o	Класът ще е - "Economy class"
 # o	Според сезона колата и цената ще са:
    # 	Лято – Кабрио – 35% от бюджета
    # 	Зима – Джип – 65% от бюджета
# car_class = str(0)
car_price = 0
if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car_price = budget * 0.35
        type_car = 'Cabrio'
    elif season == 'Winter':
        car_price = budget * 0.65
        type_car = 'Jeep'
 # •	При бюджет по-голям от 100лв. и по-малък или равен от 500лв.:
 # o	Класът ще е - "Compact class"
 # o	Според сезона колата и цената ще са:
      # 	Лято – Кабрио – 45% от бюджета
      # 	Зима – Джип – 80% от бюджета

elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_price = budget * 0.45
        type_car = 'Cabrio'
    elif season == 'Winter':
        car_price = budget * 0.80
        type_car = 'Jeep'

# •	При бюджет по-голям от 500лв.:
# o	Класът ще е – "Luxury class"
# o	За всеки сезон колата ще е джип и цената ще е:
# 	90% от бюджета

elif budget > 500:
    car_class = 'Luxury class'
    if season == 'Summer':
        car_price = budget * 0.90
        type_car = 'Jeep'

    elif season == 'Winter':
        car_price = budget * 0.90
        type_car = 'Jeep'

# Изход
# На конзолата трябва да се отпечатат два реда.
print(f"{car_class}")
# •	Първи ред – "{Вид на класа}"
# o	"Economy class", "Compact class" или "Luxury class"
print(f"{type_car} - {car_price:.2f}")
# •	Втори ред – "{Вид на колата} - {цена на колата}"
# o	Видът на колата – "Cabrio" или "Jeep"
# o	Цената трябва да е форматирана до втория знак след запетаята