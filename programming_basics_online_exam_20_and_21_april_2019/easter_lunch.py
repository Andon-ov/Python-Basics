# Задача 1. Великденски обяд

#  Цените на продуктите са следните:
# •	Козунак  – 3.20 лв.
# •	Яйца –  4.35 лв. за кора с 12 яйца
# •	Курабии – 5.40 лв. за килограм
# •	Боя за яйца - 0.15 лв. за яйце
# Вход

number_of_easter_cakes = int(input())
number_of_eggshells = int(input())
kilograms_of_cookies = int(input())
number_of_egg = number_of_eggshells * 12
sum = (number_of_easter_cakes * 3.20) + (kilograms_of_cookies * 5.40) + (number_of_eggshells * 4.35) + \
      (number_of_egg * 0.15)
print(f'{sum:.2f}')



# Изход
# Да се отпечата на конзолата колко ще са разходите по приготвянето на обяда.
# Сумата да бъде форматирана до втория знак след десетичната запетая.
