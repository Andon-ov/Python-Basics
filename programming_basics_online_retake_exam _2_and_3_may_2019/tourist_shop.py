# Задача 4. Туристически магазин
# Вашата задача е да напишете програма, която да изчислява, стойността на екипировката, както и дали определения бюджет
# е достатъчен или не, като се знае, че в магазина има следната промоция: Всеки трети продукт е на половин цена.
# Вход
# От конзолата се чете:
# •	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
# •	След това поредица от два реда (до получаване на команда "Stop" или при заявка за купуване на продукт,
# чиято стойност е по-висока от наличния бюджет) :
# o	Име на продукта – текст
# o	Цена на продукта – реално число в интервала [1.00… 5000.00]

budget = float(input())
name_of_product = input()
count = 1
total = 0

while name_of_product != "Stop":

    price_of_product = float(input())

    if count % 3 == 0:
        price_of_product /= 2
    if price_of_product > budget:
        print(f"You don't have enough money!")
        print(f"You need {abs(total - budget)} leva!")
        break
    else:
        total += price_of_product

        if total > budget:
            print(f"You don't have enough money!")
            print(f"You need {(abs(total - budget)):.2f} leva!")
            break



    count += 1
    name_of_product = input()


else:
    print(f'You bought {count - 1 } products for {total:.2f} leva.')


