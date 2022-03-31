# Задача 3. Великденска екскурзия

# Дестинация	21-23 март	24-27 март	28-31 март
# Франция	      30 лв.	    35 лв.	    40 лв.
# Италия	      28 лв.	    32 лв.	    39 лв.
# Германия	      32 лв.	    37 лв.	    43 лв.

# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - дестинация - текст с възможности "France", "Italy" или "Germany"
# •	Втори ред - дати, през които си е резервирала екскурзията - текст  с възможности "21-23","24-27" или "28-31"
# •	Трети ред - брой нощувки - цяло число в интервала [1… 100]
destination = input()
dates = input()
number_of_nights = int(input())
price = 0
if destination == "France":
    if dates == "21-23":
        price = 30
    elif dates == "24-27":
        price = 35
    elif dates == "28-31":
        price = 40
elif destination == "Italy":
    if dates == "21-23":
        price = 28
    elif dates == "24-27":
        price = 32
    elif dates == "28-31":
        price = 39
elif destination == "Germany":
    if dates == "21-23":
        price = 32
    elif dates == "24-27":
        price = 37
    elif dates == "28-31":
        price = 43
sum = price * number_of_nights
print(f"Easter trip to {destination} : {sum:.2f} leva.")

