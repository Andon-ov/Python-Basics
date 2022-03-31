# До команда "STOP" получавате заглавия на любими ваши филми. Най-добрият филм за вас ще бъде този,
# който има най-много точки. Точките се изчисляват като сбор от ASCII стойностите на символите в заглавието на филма.
# (няма да има случай, в който имаме два филма с равен брой точки)
# При изчислението на точките трябва да се има предвид следното:

# •	За всяка малка буква в заглавието, от сумата трябва да се извади два пъти дължината на заглавието на филма.
# •	За всяка главна буква в заглавието, от сумата трябва да се извади дължината на заглавието на филма.

# Може да имате максимум 7 заглавия на филми.


# Вход
# От конзолата се четат редове до команда "STOP" или до достигането на лимита от 7 филма:
# •	Заглавие на филм  – текст;

command = str(input())
sum_of_symbols = 0
count = 1
best_movie = ''
best_score = 0
while command != "STOP":

    for letter in command:
        sum_of_symbols += ord(letter)
        if 65 <= ord(letter) <= 90:
            sum_of_symbols -= len(command)
        elif 97 <= ord(letter) <= 122:
            sum_of_symbols -= (len(command)*2)

    if sum_of_symbols > best_score:
        best_movie = command
        best_score = sum_of_symbols


    if count == 7:
        print(f"The limit is reached.")
        break
    sum_of_symbols = 0
    command = str(input())
    count += 1

# На конзолата да се отпечата:
# •	Ако сте достигнали лимита от 7 филма трябва да отпечатате:
#
# Да се отпечата най-добрият филм за вас:
print(f"The best movie for you is {best_movie} with {best_score} ASCII sum.")