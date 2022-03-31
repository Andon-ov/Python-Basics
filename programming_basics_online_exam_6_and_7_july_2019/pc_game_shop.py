# Задача 5. Магазин за компютърни игри
# Процентите трябва да бъдат разделени на четири части, три заглавия на игри и всички останали :
# •	Hearthstone
# •	Fornite
# •	Overwatch
# •	Others
# Вход
# От конзолата се четат:
# •	Брой продадени игри- n - цяло положително число в интервала [1… 100]
# За следващите n реда се чете по един ред:
# o	Име на игра - текст
n = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0
for i in range(n):
    game_name = input()
    if game_name == 'Hearthstone':
        hearthstone += 1
    elif game_name == 'Fornite':
        fornite += 1
    elif game_name == 'Overwatch':
        overwatch += 1
    elif game_name != 'Hearthstone' and game_name != 'Fornite'and game_name != 'Overwatch':
        others += 1
percentage_of_hearthstone = (hearthstone / n) * 100
percentage_of_fornite = (fornite / n) * 100
percentage_of_overwatch = (overwatch/ n) * 100
percentage_of_others = (others / n) * 100

print(f"Hearthstone - {percentage_of_hearthstone:.2f}%")
print(f"Fornite - {percentage_of_fornite:.2f}%")
print(f"Overwatch - {percentage_of_overwatch:.2f}%")
print(f"Others - {percentage_of_others:.2f}%")



# Изход
# На конзолата да се изпишат четири реда:
# 	"Hearthstone - {процент продажби на Hearthstone}%"
# 	"Fornite - {процент продажби на Fornite}%"
# 	"Overwatch - {процент продажби на Overwatch}%"
# 	"Others - {процент продажби на всички останали игри}%"
# Резултатът да бъде закръглен до втората цифра след десетичния знак.
