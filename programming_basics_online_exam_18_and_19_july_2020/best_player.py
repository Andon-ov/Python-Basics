# Задача 5. Най-добър играч
# Пепи иска да напишете програма, чрез която да разбере кой е най-добрият играч от световното първенство.
# Информацията, която получавате ще бъде играч и колко гола е отбелязал. От вас се иска да отпечатате кой е
# играчът с най-много голове и дали е направил хет-трик. Хет-трик е, когато футболистът е вкарал 3 или
# повече гола. Ако футболистът е вкарал 10 или повече гола, програмата трябва да спре.
# Вход:
# От конзолата се четат по два реда до въвеждане на команда "END":
# • Име на играч – текст
# • Брой вкарани голове – цяло положително число в интервала [1 … 10000]
# Изход:
# На конзолата да се отпечатат 2 реда :
#  На първия ред:
#  "{име на играч} is the best player!"
#  На втория ред :
# o Ако най-добрият футболист е направил хеттрик:
#  "He has scored {брой голове} goals and made a hat-trick !!!"
# o Ако най-добрият футболист не е направил хеттрик:
#  "He has scored {брой голове} goals."
player_name = input()
max_goal = 0
best_player = ''
# От конзолата се четат по два реда до въвеждане на команда "END":
while player_name != "END":

    numbers_of_goal = int(input())
    if numbers_of_goal > max_goal :
        max_goal = numbers_of_goal
        best_player = player_name





    # Ако футболистът е вкарал 10 или повече гола, програмата трябва да спре.
    if numbers_of_goal >= 10:

        break



    player_name = input()

if max_goal >= 3:
    print(f'{best_player} is the best player!')
    print(f'He has scored {max_goal} goals and made a hat-trick !!!')
elif max_goal < 3:
    print(f'{best_player} is the best player!')
    print(f"He has scored {max_goal} goals.")


