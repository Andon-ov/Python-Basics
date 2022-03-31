# Задача 5. Грижи за кученце
#Да се напише програма, която проверява дали количеството храна, което е закупено за кученцето,
# ще е достатъчно докато кученцето бъде осиновено.
# Вход
# От конзолата се прочитат:



# •	Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
food = int(input())
# •	На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда кученцето на всяко
# хранене - цяло число в интервала [10 …1000]
command = input()
food_in_gr = food * 1000
sum_food = 0
while command != 'Adopted':

    if food_in_gr >= int(command):
        sum_food += int(command)

    command = input()

if food_in_gr >= sum_food:
    print(f'Food is enough! Leftovers: {food_in_gr - sum_food} grams.')
elif sum_food > food_in_gr:
    print(f'Food is not enough. You need {abs(sum_food - food_in_gr)} grams more.')



# Изход
# На конзолата се отпечатва 1 ред:
# •	Ако количеството храна е достатъчно да се отпечата:
#  	"Food is enough! Leftovers: {останала храна} grams."
# •	Ако количеството храна не е достатъчно да се отпечата:
#  	"Food is not enough. You need {нужно количество храна} grams more."