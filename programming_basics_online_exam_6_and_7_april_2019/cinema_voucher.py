# Задача 4. Кино ваучер

# Вашата задача е да напишете програма, която да изчислява колко покупки от киното може да си купи Любо
# със спечеленият ваучер. Ако името на покупката съдържа повече от 8 символа, то тя е билет за филм,
# а нейната цена представлява сумата на ASCII символите от първите ѝ два символа. Ако името на покупката съдържа 8 или
# по-малко символа, нейната цена е равна на стойността на първия ASCII символ в името. Любо въвежда името на покупките,
# които желае, докато не въведе "End" или не въведе покупка, чиято стойност е по-голяма от останалата сума на ваучера.
# Вход
# Първоначално се чете един ред:
# •	Стойността на ваучера – цяло число в интервала [1…100000]
# След това до получаване на команда "End" или до изчерпването на ваучера, се чете по един ред:
# o	Покупката, която Любо е избрал – текст


voucher = int(input())
ticket = 0
other_things = 0
total_tickets = 0
total_other = 0
price = 0
purchase = 0

while purchase != "End":
    purchase = input()
    if len(purchase) > 8:
        letter1 = purchase[0]
        letter2 = purchase[1]
        price = ord(letter1) + ord(letter2)
    elif len(purchase) <= 8:
        letter1 = purchase[0]
        price = ord(letter1)
    else:
        break

    if voucher - price >= 0:
        voucher -= price
        if len(purchase) > 8:
            ticket += 1
        elif len(purchase) <= 8 and purchase != "End":
            other_things += 1
    else:
        break

total_tickets += ticket
total_other += other_things
print(total_tickets)
print(total_other)






