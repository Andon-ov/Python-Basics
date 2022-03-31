# 4.	Магазин за детски играчки
# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите,
# които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# Вход
# От конзолата се четат 6 реда:
# 1.	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2.	Брой пъзели - цяло число в интервала [0… 1000]
# 3.	Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4.	Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5.	Брой миньони - цяло число в интервала [0 … 1000]
# 6.	Брой камиончета - цяло число в интервала [0 … 1000]
# Изход
# На конзолата се отпечатва:
# •	Ако парите са достатъчни се отпечатва:
# o	"Yes! {оставащите пари} lv left."
# •	Ако парите НЕ са достатъчни се отпечатва:
# o	"Not enough money! {недостигащите пари} lv needed."

# Резултатът трябва да се форматира до втория знак след десетичната запетая.
# Примерен вход и изход

# 40.8
# 20
# 25
# 30
# 50
# 10
# Yes! 418.20 lv left.	Сума: 20 * 2.60 + 25 * 3 + 30 * 4.10 + 50 * 8.20 + 10 * 2 = 680 лв.
# Брой на играчките: 20 + 25 + 30 + 50 + 10 = 135
# 135 > 50 => 25% отстъпка; 25% от 680 = 170 лв. отстъпка
# Крайна цена: 680 – 170 = 510 лв.
# Наем: 10% от 510 лв. = 51 лв.
# Печалба: 510 – 51 = 459 лв.
# 459 > 40.8 => 459 – 40.8 = 418.20 лв. остават
# Вход	Изход	Обяснения
# 320
# 8
# 2
# 5
# 5
# 1
# Not enough money! 238.73 lv needed.	Сума: 8 * 2.60 + 2 * 3 + 5 * 4.10 + 5 * 8.20 + 1 * 2 = 90.3 лв.
# Брой на играчките: 8 + 2 + 5 + 5 + 1 = 21
# 21 < 50 => няма отстъпка
# Наем: 10% от 90.3 = 9.03 лв.
# Печалба: 90.3 – 9.03 = 81.27 лв.
# 81.27 < 320 => 320 – 81.27 = 238.73 лв. не достигат

trip_price = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
# общ брой играчки - ако са >= 50 - има 25 % отстъпка
number_toy = number_of_trucks + number_of_minions + number_of_puzzles + number_of_teddy_bears + number_of_talking_dolls
# Смятане на цените
puzzle_price = 2.60 * number_of_puzzles
talking_doll_price = 3 * number_of_talking_dolls
teddy_bear_price = 4.10 * number_of_teddy_bears
minion_price = 8.20 * number_of_minions
truck_price = 2 * number_of_trucks
total_sum = puzzle_price + talking_doll_price + teddy_bear_price + minion_price + truck_price
total_sum *= 0.9
if number_toy >= 50:
    total_sum *= 0.75
else:
    total_sum = total_sum
trip_chance = total_sum - trip_price
# print(trip_chance)
absolute_trip_chance = abs(trip_chance)
if total_sum >= trip_price:
    print(f"Yes! {absolute_trip_chance:.2f} lv left.")
elif trip_price >= total_sum:
    print(f"Not enough money! {absolute_trip_chance:.2f} lv needed.")