# Задача 4. Клуб
# Напише програма, която да изчислява приходите на един клуб за вечерта и дали е достигната желаната печалба,
# като знаете следните условия: цената на един коктейл е дължината неговото име.
# Ако цената на една поръчка е нечетно число, има 25% отстъпка от цената на поръчката.
# Вход
# От конзолата се четат:
# •	На първия ред – желаната печалба на клуба - реално число в интервала [1.00... 15000.00]
# Поредица от два реда до получаване на командата "Party!" или до достигане на желаната печалба:
# o	Име на коктейла – текст
# o	Брой на коктейлите за поръчката – цяло число в интервала [1… 50]

desired_profit = float(input())
# Поредица от два реда до получаване на командата "Party!" или до достигане на желаната печалба:+
cocktail_name = input()
final_sum = 0
sum = 0
have_desired_profit = False

while cocktail_name != "Party!":


    number_of_cocktails = int(input())

# Ако цената на една поръчка е нечетно число, има 25% отстъпка от цената на поръчката.
# цената на един коктейл е дължината неговото име
    price = len(cocktail_name)
    sum += int(price) * number_of_cocktails
    if sum % 2 != 0:
        sum *= 0.75

    final_sum += sum
    sum = 0
    if final_sum >= desired_profit:
        have_desired_profit = True
        break
    cocktail_name = input()

if have_desired_profit:
    print(f"Target acquired.")
    print(f"Club income - {final_sum:.2f} leva.")
else:
    print(f"We need {(abs(desired_profit - final_sum)):.2f} leva more.")
    print(f"Club income - {final_sum:.2f} leva.")

# Изход
# На конзолата първо да се отпечата един ред:
# •	При получена команда "Party!":
#  "We need {недостигаща сума} leva more."
# •	При достигане на желаната печалба:
# 	"Target acquired."
# След това да се отпечата:
# 	"Club income - {приходи от клуба} leva."
# Парите да бъдат форматирани до втората цифра след десетичния знак.
# #