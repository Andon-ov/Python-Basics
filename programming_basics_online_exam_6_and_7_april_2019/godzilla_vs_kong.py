# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да
# напишете програма, която да изчисли, дали предвидените средства са достатъчни за снимането на филма.
# За снимките ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:

#  Декорът за филма е на стойност 10% от бюджета.
#  При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

# От конзолата се четат 3 реда:
# Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

# На конзолата трябва да се отпечатат два реда:
#  Ако парите за декора и дрехите са повече от бюджета:
# o "Not enough money!"
# o "Wingard needs {парите недостигащи за филма} leva more."
#  Ако парите за декора и дрехите са по малко или равни на бюджета:
# o "Action!"
# o "Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.
budget = float(input())
number_of_statistics = int(input())
price_for_clothing = float(input())
need_money = 0
decor = budget * 0.1
total = 0
if number_of_statistics > 150:
    price_for_clothing *= 0.90
need_money = (number_of_statistics * price_for_clothing) + decor
total = abs(budget - need_money)
if need_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {total:.2f} leva more.")
elif need_money <= budget:
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")