# 6.	Домашни любимци
# Марина обича да пътува. Тя има 3 домашни любимеца (куче, котка и костенурка).
# Когато заминава на пътешествие трябва да съобрази колко храна да им остави, за да не останат гладни.
# Напишете програма, която пресмята колко килограма храна ще изядат всички за времето,
# в което Марина отсъства и дали оставената храна от нея ще им е достатъчна.
# Всяко животно изяжда определено количество храна на ден.
# Вход
# От конзолата се четат пет реда:
import math

days = int(input())
left_food_kg = int(input())
dog_food_for_day_kg = float(input())
cat_food_for_day_kg = float(input())
turtle_food_for_day_gr = float(input())
turtle_food_for_day_kg = turtle_food_for_day_gr / 1000
all_needed_food = (dog_food_for_day_kg + cat_food_for_day_kg + turtle_food_for_day_kg) * days
needed_food = abs(all_needed_food - left_food_kg)
if left_food_kg >= all_needed_food:
# •	Ако оставената храна Е достатъчна:
    print(f'{math.floor(needed_food)} kilos of food left.')
else:
# •	Ако оставената храна НЕ Е достатъчна:
    print(f'{math.ceil(needed_food)} more kilos of food are needed.')

