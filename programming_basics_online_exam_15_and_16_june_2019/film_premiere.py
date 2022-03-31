# Задача 3. Филмова премиера
# За предстояща премиера на три известни продукции, местно кино ви наема да напишете софтуер, който да изчислява цената,
# която клиентите трябва да заплатят, според филма и пакета, който са избрали.

# 	        John Wick	    Star Wars	    Jumanji
# Напитка	12 лв./бр.	    18 лв. /бр.	    9 лв. /бр.
# Пуканки	15 лв. /бр.	    25 лв. /бр.	    11 лв. /бр.
# Меню	    19 лв. /бр.	    30 лв. /бр.	    14 лв. /бр.

# Напишете програма, която изчислява цената, която трябва да се заплати, като имате в предвид следните отстъпки:



# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
# •	Втори ред - пакет за филм - текст  с възможности "Drink", "Popcorn" или "Menu"
# •	Трети ред - брой билети - цяло число в интервала [1… 30]

projection = input()
movie_package = input()
number_of_tickets = int(input())
total_price = 0
if projection == "John Wick":
    if movie_package == "Drink":
        total_price = number_of_tickets * 12
    elif movie_package == "Popcorn":
        total_price = number_of_tickets * 15
    elif movie_package == "Menu":
        total_price = number_of_tickets * 19
elif projection == "Star Wars":
    if movie_package == "Drink":
        total_price = number_of_tickets * 18
    elif movie_package == "Popcorn":
        total_price = number_of_tickets * 25
    elif movie_package == "Menu":
        total_price = number_of_tickets * 30
elif projection == "Jumanji":
    if movie_package == "Drink":
        total_price = number_of_tickets * 9
    elif movie_package == "Popcorn":
        total_price = number_of_tickets * 11
    elif movie_package == "Menu":
        total_price = number_of_tickets * 14
# •	При избран филм "Star Wars" и закупени поне четири билета, има 30% семейна отстъпка.
# •	При избран филм "Jumanji" и закупени точно два билета, има 15% отстъпка за двама.
if projection == "Star Wars" and number_of_tickets >= 4:
    total_price *= 0.70
if projection == "Jumanji" and number_of_tickets == 2:
    total_price *= 0.85
print(f"Your bill is {total_price:.2f} leva.")

