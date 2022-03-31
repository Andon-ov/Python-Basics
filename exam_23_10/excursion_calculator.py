# Вход:
# 1.	Първи ред – брой хора – цяло число в интервала [1 … 20]
# 2.	Втори ред – сезон – текст с възможности - "spring", "summer", "autumn" или "winter"

number_of_people = int(input())
season = input()
sum = 0
# 	             Пролет (spring)	     Лято (summer)	     Есен (autumn)	     Зима (winter)
#  До 5 човека	  50.00 лв. на човек	48.50 лв. на човек	 60.00 лв. на човек	 86.00 лв. на човек
#  Над 5 човека	 48.00 лв. на човек	     45.00 лв. на човек	 9.50 лв. на човек	 85.00 лв. на човек
if number_of_people <= 5:
    if season == "spring":
        sum = number_of_people * 50
    elif season == "summer":
        sum = number_of_people * 48.50
    elif season == "autumn":
        sum = number_of_people * 60
    elif season == "winter":
        sum = number_of_people * 86
elif number_of_people > 5:
    if season == "spring":
        sum = number_of_people * 48
    elif season == "summer":
        sum = number_of_people * 45
    elif season == "autumn":
        sum = number_of_people * 49.50
    elif season == "winter":
        sum = number_of_people * 85
        # •    При
        # "summer" -> 15 % отстъпка
        # •    При
        # "winter" -> 8 % оскъпяване
if season == "summer":
    sum *= 0.85
elif season == "winter":
    sum *= 1.08

print(f"{sum:.2f} leva.")
