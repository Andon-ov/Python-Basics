# Задача 6. Висок скок
#
# Вашата задача е да напишете софтуер, с който Иванов да следи своя прогрес и дали е достигнал желаните резултати.
# В началото програмата получава желаната височина на летвата от Тихомир, той започва тренировката си като поставя
# летвата на височина 30см по-ниско от целта.
# За всяка височина той има право на 3 скока, като за да бъде един скок успешен, той трябва да бъде над височината
# на летвата. При успешен скок (над летвата), височината й се вдига с
# 5 сантиметра. При три неуспешни скока на една и съща височина, тренировката приключва с неуспех. При достигане на
# желаната височина и нейното успешно прескачане, тренировката приключва с успех.
# Вход
# Входът е поредица от цели числа в интервала [100…300]:
# •	На първия ред се прочита желаната от Тихомир Иванов височина в сантиметри
# •	На всеки следващ ред до приключване на програмата се прочита височината от скока на Иванов
target_height = int(input())
stick_height = target_height - 30
all_jumps = 0

while stick_height <= target_height:
    count_failed_jumps = 0

    for i in range(1, 4):
        all_jumps += 1
        jump_height = int(input())

        if jump_height > stick_height:
            stick_height += 5
            break
        else:
            count_failed_jumps += 1

    if count_failed_jumps == 3:
        print(f"Tihomir failed at {stick_height}cm after {all_jumps} jumps.")
        break
else:
    print(f"Tihomir succeeded, he jumped over {target_height}cm after {all_jumps} jumps.")


# Изход
# На конзолата трябва да се отпечата един ред:
# •	Ако Тихомир не успее да преодолее желаната височина:
# o	"Tihomir failed at {височина на летвата към момента на провала}cm after {брой скокове от началото на тренировката} jumps."
# •	Ако Тихомир успее да преодолее височината:
# o	"Tihomir succeeded, he jumped over {височина на прескочената последно летва}cm after {брой скокове за цялата тренировка} jumps."





# ОТРИЦАТЕЛЕН ВАРИЯНТ

# target_height = int(input())
# current_height = target_height - 30
#
# total_jumps = 0
# failed = False
# counter_failed = 0
#
# while not failed:
#     jump = int(input())
#     total_jumps = total_jumps + 1
#
#     if jump <= current_height:
#         counter_failed = counter_failed + 1
#         if counter_failed == 3:
#             failed = True
#     else:
#         if current_height >= target_height:
#             break
#         current_height = current_height + 5
#         counter_failed = 0
#
# if not failed:
#     print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_jumps} jumps.")
# else:
#     print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
