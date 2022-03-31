# Задача 3. Боядисване на яйца

# 					Червено (Red)	Зелено (Green)	Жълто (Yellow)
# Големи (Large)		16 лв.			12 лв.			9 лв.
# Средни (Medium)		13 лв.			9 лв.			7 лв.
# Малки (Small)			9 лв.			8 лв.			5 лв.

# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред – размер на яйцата – текст с възможности "Large", "Medium" или "Small"
# •	Втори ред – цвят на яйцата – текст  с възможности "Red", "Green" или "Yellow"
# •	Трети ред – брой партиди – цяло число в интервала [1… 350]

egg_size = input()
egg_color = input()
number_of_batches = int(input())
price = 0
if egg_size == "Large":
	if egg_color == "Red":
		price = 16
	elif egg_color == "Green":
		price = 12
	elif egg_color == "Yellow":
		price = 9
elif egg_size == "Medium":
	if egg_color == "Red":
		price = 13
	elif egg_color == "Green":
		price = 9
	elif egg_color == "Yellow":
		price = 7
elif egg_size == "Small":
	if egg_color == "Red":
		price = 9
	elif egg_color == "Green":
		price = 8
	elif egg_color == "Yellow":
		price = 5
sum = (price * number_of_batches) * 0.65

# С 35% от крайната цена ще бъдат покрити производствени разходи
print(f"{sum:.2f} leva.")

