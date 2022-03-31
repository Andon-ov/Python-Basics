# Задача 3. Карта за фитнес
# Да се напише програма, която проверява дали първоначално налична сума е достатъчна, за да се заплати
# карта за месечен достъп във фитнес.
# Цената на картата зависи от пола на клиента и спорта, който практикува:
# Пол Gym Boxing Yoga Zumba Dances Pilates
# мъж $42 $41 $45 $34 $51 $39
# жена $35 $37 $42 $31 $53 $37
# Всички цени на карти за ученици (възраст под 19 години вкл.) са с 20% намаление.
# Вход
# От конзолата се прочитат 4 реда:
#  Сумата, с която разполагаме - реално число в интервала [10.00…1000.00]
#  Пол - символ ('m' за мъж и 'f' за жена)
#  Възраст - цяло число в интервала [5…105]
#  Спорт - текст (една от възможностите в таблицата)
# Изход
# На конзолата се отпечатва 1 ред:
#  Ако сумата е достатъчна:
# "You purchased a 1 month pass for {sport}."
# където {sport} е въведения тип спорт
#  Ако сумата не е достатъчна трябва да се пресметне колко още пари са необходими, за да се закупи
# карта:
# "You don't have enough money! You need ${money} more."
# където {money} e оставащата сума нужна, за да се закупи картата, форматирана до втория знак след
# десетичната запетая.

amount = float(input())
gender = input()
age = int(input())
sports = input()
price = 0

if gender == 'm':
    if sports == 'Gym':
        price = 42
    elif sports == 'Boxing':
        price = 41
    elif sports == 'Yoga':
        price = 45
    elif sports == 'Zumba':
        price = 34
    elif sports == 'Dances':
        price = 51
    elif sports == 'Pilates':
        price = 39
elif gender == 'f':
    if sports == 'Gym':
        price = 35
    elif sports == 'Boxing':
        price = 37
    elif sports == 'Yoga':
        price = 42
    elif sports == 'Zumba':
        price = 31
    elif sports == 'Dances':
        price = 53
    elif sports == 'Pilates':
        price = 37
if age <= 19:
    price *= 0.8
totall = abs(amount - price)
if amount >= price:
    print(f"You purchased a 1 month pass for {sports}.")
else:
    print(f"You don't have enough money! You need ${totall:.2f} more.")