# Задача 4.Тренировка
# Започвайки тренировка, първия ден тя пробягва М километра.
# Следващите N дни, тя увеличава дневната си норма с К%. За да успее да отслабне, тя трябва да избяга минимум 1 000 км.
# Съставете програма, която при получени начални километри, брой дни и проценти, с които тя ще
# увеличава всеки ден нормата си, ще проверява дали километрите, които тя е избягала са достатъчни.
# Ако километрите не са достатъчни, на конзолата да се изведат недостигащите километри.
# Ако са достатъчни да се изведе съобщение в което г-жа Иванова е поздравена за добре свършената работа.
# Вход:
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – N – брой дни, в които г-жа Иванова тренира  – цяло число в интервала [1...50]
# •	На втория ред – M – километрите, които е избягала първия ден – реално число в интервала [1.00…500.00]
# •	За всеки един ден на отделен ред :
# 	Процентите, с които се увеличава дневната си норма – цяло число в интервала [1…100]

import math
numbers_of_days = int(input())
first_day_run = float(input())
total_run = 0 + first_day_run

for i in range(1,numbers_of_days):
    percent = int(input())
    daily_run = (total_run/100) * percent
    total_run += daily_run

if total_run >= 1000:
    print(f"You've done a great job running {math.ceil(abs(total_run - 1000))} more kilometers!")
elif total_run < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(abs(total_run - 1000))} more kilometers")

# import math
# n = int(input())
# m = float(input())
# total = 0
# total_sum = 0
# for i in range(n):
#
#     percent = int(input())
#
#
#     if i == 0:
#         sum = m * ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 1:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#
#     elif i == 2:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 3:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 4:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 5:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 6:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 7:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 7:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 8:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 9:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#     elif i == 10:
#         sum *= ((percent + 100) / 100)
#         total_sum += sum
#
# if (total_sum + m) >= 1000:
#     print(f"You've done a great job running {math.ceil(abs((total_sum + m) - 1000))} more kilometers!")
# elif (total_sum + m) < 1000:
#     print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(abs((total_sum + m) - 1000))} more kilometers")


# 1 ден: 30 км
# 2 ден: 30 + 10% = 33 км
# 3 ден: 33 + 15% = 37.95 км
# 4 ден: 37.95 + 20% = 45.54 км
# 5 ден: 45.54 + 5% = 47.817 км
# 6 ден: 47.817 + 12% = 53.55504 км


# Изход:
# Да се отпечата на конзолата 1 ред, както следва:
# •	Ако пробяганите километри са >= 1 000 км – да се отпечатва съобщение:
# "You've done a great job running {избяганите километри повече от 1000} more   kilometers!"
# •	 Ако пробяганите километри са < 1 000 км – да се отпечата съобщение:
# "Sorry Mrs. Ivanova, you need to run {недостигащите километри} more kilometers"
# Резултатът да се форматира до по-голямото цяло число.
