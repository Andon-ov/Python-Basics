# По време на седмицата на Оскарите, градското кино пуска прожекции на някои от филмите, които са
# номинирани в категорията за "Най-добър филм". В таблицата са показани кои са филмите и каква е цената
# за прожекция спрямо залата, в която се прожектира филмът.
# Филм normal luxury ultra luxury
# A Star Is Born 7.50 лв. 10.50 лв. 13.50 лв.
# Bohemian Rhapsody 7.35 лв. 9.45 лв. 12.75 лв.
# Green Book 8.15 лв. 10.25 лв. 13.25 лв.
# The Favourite 8.75 лв. 11.55 лв. 13.95 лв.
# Напишете програма, която изчислява какъв е приходът от даден филм, като знаете в какъв тип зала се
# прожектира и колко човека са си купили билет за прожекцията.

# Входът се чете от конзолата и се състои от три реда:
#  Първи ред – име на филм – текст ("A Star Is Born", "Bohemian Rhapsody","Green Book" или "The Favourite")
#  Втори ред– вид на залата – текст ("normal", "luxury" или "ultra luxury")
#  Трети ред – брой на закупените билети – цяло число в интервала [1…100]

# На конзолата трябва да се отпечата един ред:
# "{име на филма} -> {приходи от прожекцията на филма} lv."
# Приходите да бъдат закръглени до втория знак след десетичната запетая.
movie_name = input()
hall_type = input()
number_tickets = int(input())
revenue_from_screening = 0
price = 0
if hall_type == 'normal':
    if movie_name == 'A Star Is Born':
        price = 7.5
    elif movie_name == 'Bohemian Rhapsody':
        price = 7.35
    elif movie_name == 'Green Book':
        price = 8.15
    elif movie_name == 'The Favourite':
        price = 8.75
elif hall_type == 'luxury':
    if movie_name == 'A Star Is Born':
        price = 10.50
    elif movie_name == 'Bohemian Rhapsody':
        price = 9.45
    elif movie_name == 'Green Book':
        price = 10.25
    elif movie_name == 'The Favourite':
        price = 11.55
elif hall_type == 'ultra luxury':
    if movie_name == 'A Star Is Born':
        price = 13.50
    elif movie_name == 'Bohemian Rhapsody':
        price = 12.75
    elif movie_name == 'Green Book':
        price = 13.25
    elif movie_name == 'The Favourite':
        price = 13.95
revenue_from_screening = number_tickets * price
print(f"{movie_name} -> {revenue_from_screening:.2f} lv.")