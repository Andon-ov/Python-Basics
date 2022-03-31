# Задача 4. Игра на карти "Number wars"
# "Numbers" е нова игра, която се играе с 36 карти (двойки, тройки, четворки, петици, шестици, седмици, осмици,
# деветки и десетки от всички 4 бои). Правилата на играта са следните:
# 	Играе се от двама играчи, които започват с равен брой карти
# 	На всяко раздаване всеки един от тях дава по 1 карта:
# o	Ако картата на първия играч е с по-голяма стойност от картата на втория играч, първият получава точки,
# които са равни на разликата между картата на първия и картата на втория (например: първият дава тройка купа,
# а вторият двойка каро -> първият печели, защото 3 > 2 и точките, които печели, са 3 – 2 = 1).
# o	Ако картата на втория играч е с по-голяма стойност от картата на първия играч, вторият получава точки,
# които са равни на разликата между картата на втория и картата на първия (например: вторият дава осмица пика,
# а първият шестица спатия -> вторият печели, защото 8 > 6 и точките, които печели, са 8 – 6 = 2).
# o	Ако картите, които дават двамата, са с еднаква стойност, тогава се получава "Number wars"
# и всеки един от играчите трябва да даде по още една карта. Играчът, чиято карта е с по-голяма стойност,
# печели и играта приключва(В този случай, няма да има еднакви карти).
# 	Освен при "Number wars", играта може да приключи и при команда "End of game".
# Тогава никой не печели и играта приключва.
# Вход
# Първоначално се четат два реда:
# •	Име на първия играч - текст
# •	Име на втория играч - текст
# След това, до получаване на команда "End of game", се четат многократно по два реда:
# 1.	Карта, която дава първият играч- цяло число в интервала [2…9]
# 2.	Карта, която дава вторият играч -  цяло число в интервала [2…9]
# При еднакви карти на двамата играчи се прочитат нови два реда (карта, която дава първият и карта, която дава вторият.)

name_player_one = input()
name_player_two = input()
card_player_one = int(input())
card_player_two = int(input())
player_one_point = 0
player_two_point = 0


while card_player_one != "End of game" or card_player_two != "End of game":
    card_player_one = int(input())
    card_player_two = int(input())

    if card_player_one > card_player_two:
        player_one_point += card_player_one - card_player_two
    elif card_player_two > card_player_one:
        player_two_point += card_player_two - card_player_one
    else:
        print("Number wars!")
        card_player_one = int(card_player_one)
        card_player_two = int(card_player_two)

        if card_player_one > card_player_two:
            print(f"{name_player_one} is winner with {player_one_point} points")
            break
        else:
            print(f"{name_player_two} is winner with {player_two_point} points")
            break
    card_player_one = input()
    if card_player_one == "End of game":
        print(f"{player_one_point} has {player_one_point} points")
        print(f"{player_two_point} has {player_two_point} points")
        break
    card_player_two = input()



# Изход
# При случая, в който има "Number wars ", да се отпечата:
# •	"Number wars!"
# •	"{име на победителя} is winner with {брой натрупани точки} points"
# При команда "End of game" да се отпечатат два реда:
# •	"{име на първия играч} has {брой натрупани точки за първия играч} points"
# •	"{име на втория играч} has {брой натрупани точки за втория играч} points"
