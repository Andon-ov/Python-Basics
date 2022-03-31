# Задача 6. Смени
# Любимият отбор на Пепи е на финал, но започва да губи мача. Треньорът на отбора не знае какви смени да направи,
# за да обърне резултата. Напишете програма, с която ще разберете кой са първите 6 смени, които могат да се направят.
# Знаем, че всяка цифра от двата номера е в даден интервал. За да бъде възможна една смяна,
# първата цифра от номера трябва да бъде четна, а втората -  нечетна.
# Вход:
# От конзолата се четат 4 реда:
# •	K - началото на интервала за първото число от първия номер – цяло число в интервала [0..8]
# •	L - началото на интервала за второто число от първия номер – цяло число в интервала [9..0]
# •	M - началото на интервала за първото число от втория номер – цяло число в интервала [0..8]
# •	N - началото на интервала за второто число от втория номер – цяло число в интервала [9..0]
# Изход:
# На конзолата да се отпечатат първите 6 възможни смени по следния начин:
# •	Ако смяната е възможна и номерата НЕ съвпадат, да се отпечата:
# "{K}{L} - {M}{N}"
# •	Ако смяната е възможна и номерата съвпадат, да се отпечата:
# "Cannot change the same player."

k = int(input())
l = int(input())
m = int(input())
n = int(input())
count = 0

for a in range(k, 8 + 1):
    for b in range(9 , l - 1 , -1):
        for c in range(m,8 + 1):
            for d in range(9 , n - 1, -1):
                if count >= 6:
                    break

                if a % 2 == 0 and b % 2 != 0 and c % 2 == 0 and d % 2 != 0:

                    if  a == c and b == d:
                        print("Cannot change the same player.")

                    else:

                        print(f"{a}{b} - {c}{d}")
                        count += 1