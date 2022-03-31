# Задача 4. Битката на великденските яйца
# На Великден семейството на Деси се събира и тя решава да организира "битка" между великденски яйца.
# Правилата на "битката" са следните:
# •	Участват двама играчи
# •	Всеки от тях започва с определен брой яйца
# •	При получаване на команда "one" -> първият играч печели => яйцата на втория намаляват с едно
# •	При получаване на команда "two" -> вторият играч печели => яйцата на първия намаляват с едно
# •	Играта приключва, ако някой от играчите остане без яйца или до получаване на команда "End of battle"
# Вход
# Първоначално се четат два реда:
# 1.	Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
# 2.	Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
# След това до получаване на команда "End of battle" се четe многократно един ред:
# 3.	Победител - текст - "one" или "two"


number_of_eggs_of_player_one = int(input())
number_of_eggs_of_player_two = int(input())


winner = input()
while winner != "End of battle":
    if winner == "one":
        number_of_eggs_of_player_two -= 1
    elif winner == "two":
        number_of_eggs_of_player_one -= 1

    if number_of_eggs_of_player_one == 0:
        print(f"Player one is out of eggs. Player two has {number_of_eggs_of_player_two} eggs left.")
        break
    elif number_of_eggs_of_player_two == 0:
        print(f"Player two is out of eggs. Player one has {number_of_eggs_of_player_one} eggs left.")
        break
    winner = input()
else:
    print(f"Player one has {number_of_eggs_of_player_one} eggs left.")
    print(f"Player two has {number_of_eggs_of_player_two} eggs left.")


