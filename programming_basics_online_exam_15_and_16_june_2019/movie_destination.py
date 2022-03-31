# Задача 3. Дестинация за филм

# Помогнете му, като напишете програма, която изчислява колко ще му струва да заснеме филма,
# като знаете колко излиза един снимачен ден. Цената за един ден се определя от сезона и дестинацията:
#          Дестинация
# Сезон	      Dubai	      Sofia     London
# Winter	45 000 lv.	17 000 lv.	24 000 lv.
# Summer	40 000 lv.	12 500 lv.	20 250 lv.
# От конзолата се четат 4 реда:
# 1.	Бюджет на филма – реално число в диапазона [100 000.0… 2 000 000.0]
# 2.	Дестинация – текст, с възможности "Dubai", "Sofia" и "London"
# 3.	Сезон – текст, с възможности "Summer" и "Winter"
# 4.	Брой дни  – цяло число в диапазона [1… 40]

movie_budget = float(input())
destination = input()
season = input()
number_of_days = int(input())
sum = 0
if season == "Winter":
    if destination == "Dubai":
        sum = number_of_days * 45000
    elif destination == "Sofia":
        sum = number_of_days * 17000
    elif destination == "London":
        sum = number_of_days * 24000

elif season == "Summer":
    if destination == "Dubai":
        sum = number_of_days * 40000
    elif destination == "Sofia":
        sum = number_of_days * 12500
    elif destination == "London":
        sum = number_of_days * 20250

# Съществуват следните данъчни облекчения/облагания:
# •	Ако дестинацията е Дубай – 30% отстъпка от крайната цена
# •	Ако дестинацията е София – цената се оскъпява с 25%
if destination == "Dubai":
    sum *= 0.70
if destination == "Sofia":
    sum *= 1.25
diff = abs(movie_budget - sum)
if movie_budget >= sum:
# •	Ако бюджета е достатъчен:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
# •	  Ако бюджета НЕ е достатъчен:
else:
    print(f"The director needs {diff:.2f} leva more!")

