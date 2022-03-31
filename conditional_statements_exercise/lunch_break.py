# Обедна почивка
# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма,
# с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
# Изход
# На конзолата да се изпише един ред:
# •	Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# •	Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
# Времето да се закръгли до най-близкото цяло число нагоре.
from math import ceil

series_name = str(input())
episode_duration = int(input())
duration_of_rest = int(input())
# Времето за обяд ще бъде 1/8 от времето за почивка
time_for_lunch = duration_of_rest * 0.125
# Времето за отдих ще бъде 1/4 от времето за почивка.
time_for_rest = duration_of_rest * 0.25
# Свободното време = продължителноста на почивката - (времето за обяд + времето за почивка)
free_time = duration_of_rest - (time_for_lunch + time_for_rest)
# Нужното време за сериала = свободното време - продължителнодта на епизода
need_time = (free_time - episode_duration)
absolut_need_time = abs(need_time)
if need_time >= 0:
    print(f'You have enough time to watch {series_name} and left with {ceil(absolut_need_time)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(absolut_need_time)} more minutes.")

