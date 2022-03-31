# Задача 6. Великденска украса
# великденска украса – кошнички за яйца (basket), великденски венци (wreath) и шоколадови зайци (chocolate bunny).
#  изчислява каква сметка трябва да плати всеки един клиент на магазина, като се има в предвид,
# че всеки клиент закупил четен брой продукти, ще получи 20% отстъпка от крайната цена.
# След като всички клиенти приключат с покупките, трябва да се отпечата средно по колко пари е похарчил всеки човек.
# Цените на продуктите са:
# •	кошничка за яйца (basket) – 1.50 лв.
# •	великденски венец (wreath) – 3.80 лв.
# •	шоколадов заек (chocolate bunny) – 7 лв.
# Вход
# От конзолата първоначално се чете един ред:
# •	Брои на клиентите в магазина – цяло число [1… 100]
# •	След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
# o	Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")
numbers_of_clients = int(input())
sum = 0
count = 0
total_sum = 0


for i in range(numbers_of_clients):
    purchase = input()

    while purchase != "Finish":
        count += 1
        if purchase == "basket":
            sum += 1.5
        elif purchase == "wreath":
            sum += 3.8
        elif purchase == "chocolate bunny":
            sum += 7

        purchase = input()
    if count % 2 == 0:
        sum *= 0.8

    if purchase == "Finish":
        print(f"You purchased {count} items for {sum:.2f} leva.")
        total_sum += sum
        count = 0
        sum = 0

print(f"Average bill per client is: {(total_sum/ numbers_of_clients):.2f} leva.")



# Изход
# •	При получаване на командата "Finish" да се отпечата един ред:
# o	"You purchased {броя на покупките} items for {крайната цена} leva."
# •	Накрая, след като всички клиенти приключат с покупките, да се отпечата на един ред
# o	"Average bill per client is: {средно аритметично на парите които е похарчил всеки един клиент} leva."
# Всички пари трябва да бъдат форматирани до втората цифра след десетичния знак.
