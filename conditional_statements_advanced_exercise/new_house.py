# 3.Нов дом
# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма,
# която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.
# Различните цветя са с различни цени:
# цвете	               Роза	Далия	Лале  Нарцис	Гладиола
# Цена на брой в лева	5	3.80	2.80	3	     2.50
# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен
#     - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

type_flower = input()
number_flower = int(input())
budget = int(input())
price_per_piece = 0
totall = 0

if type_flower == "Roses":
    price_per_piece = 5
    if number_flower > 80:
        price_per_piece *= 0.9
elif type_flower == "Dahlias":
    price_per_piece = 3.8
    if number_flower > 90:
        price_per_piece *= 0.85
elif type_flower == "Tulips":
    price_per_piece = 2.8
    if number_flower > 80:
        price_per_piece *= 0.85
elif type_flower == "Narcissus":
    price_per_piece = 3
    if number_flower < 120:
        price_per_piece *= 1.15
elif type_flower == "Gladiolus":
    price_per_piece = 2.5
    if number_flower < 80:
        price_per_piece *= 1.20
totall = price_per_piece * number_flower
money_lef = abs(budget - totall)
if budget >= totall:
    print(f"Hey, you have a great garden with {number_flower} {type_flower} and {money_lef:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_lef:.2f} leva more.")


