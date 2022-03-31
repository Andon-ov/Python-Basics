# Задача 2. Скелетон
# Вашата програма получава контролата в минути, която трябва да бъде достигната или подобрена, за да може
# Марин да вземе квота. Също така програмата ще получи разстоянието на улея в метри, и времето в секунди,
# за което той изминава 100 метра.
# Трябва да се има предвид, че поради наклона на улея, на всеки 120 метра неговото време намаля с 2.5 секунди.
# Вход
# От конзолата се четат 4 реда:
# Ред 1.	Минути на контролата – цяло число в интервала [0…59]
# Ред 2.	Секунди на контролата – цяло число в интервала [0…59]
# Ред 3.	Дължината на улея в метри – реално число в интервала [0.00…50000]
# Ред 4.	Секунди за изминаване на 100 метра – цяло число в интервала [0…1000]

minutes_of_control = int(input())
seconds_of_control = int(input())
length_of_the_chute_in_meters = float(input())
seconds_to_travel_100_meters = int(input())
time = 0
olympic_quota = (minutes_of_control * 60) + seconds_of_control
time = (length_of_the_chute_in_meters / 100) * seconds_to_travel_100_meters
slope_of_chute = length_of_the_chute_in_meters / 120
time -= slope_of_chute * 2.5
if time <= olympic_quota:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:

# Изход
# На конзолата трябва да се отпечата на един или два реда:
# •	Ако времето на Марин е по-малко или равно на контролата:

# •	Ако времето на Марин е повече от това на контролата:
    print(f"No, Marin failed! He was {abs(time - olympic_quota):.3f} second slower.")
# Резултатът трябва да е форматиран до третия знак след десетичния знак.
