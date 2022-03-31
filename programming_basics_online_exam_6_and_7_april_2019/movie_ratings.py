# Задача 5. Филмов рейтинг
# Напишете програма, която показва кой филм е с най-висок рейтинг, кой е с най-нисък и колко е средният рейтинг от
# всички филми, които си е набелязала да гледа.


# Вход
# От конзолата първо се чете един ред:
# •	Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
# За всеки филм се прочитат два отделни реда:
# •	Име на филма – текст
# •	Рейтинг на филма - реално число в интервала [1.00…10.00]
import sys

nomber_of_movies = int(input())
max_rating = 0
max_movie = ''
min_rating = sys.maxsize
min_movie = ''
average = 0

for i in range(nomber_of_movies):
    movie_name = input()
    movie_rating = float(input())
    average += movie_rating

    if movie_rating > max_rating:
        max_rating = movie_rating
        max_movie = movie_name
    elif movie_rating < min_rating:
        min_rating = movie_rating
        min_movie = movie_name

print(f"{max_movie} is with highest rating: {max_rating}")
print(f'{min_movie} is with lowest rating: {min_rating}')
print(f"Average rating: {average / nomber_of_movies:.1f}")


# Изход
# Отпечатват се три реда в следния формат:
# •	"{име на филма с най-висок рейтинг} is with highest rating: {рейтинг на филма}"
# •	"{име на филма с най-нисък рейтинг} is with lowest rating: {рейтинг на филма}"
# •	"Average rating: {средният рейтинг на всички филми}"
# Максималният, минималният и средният рейтинг да се форматира до първата цифра след десетичния знак.
