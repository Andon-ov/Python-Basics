# Задача 6. Игра на имена

# Всеки играч написва името си, след това за всяка една буква от името си написва по едно цяло число,
# ако числото съвпада с ASCII стойността на съответната буква, играчът получава 10 точки, в противен случай,
# получава само 2 точки. Победител е играчът с най-много точки в края на играта. В случай,
# че двама играчи имат равен брой точки, печели този, който втори е достигнал резултата.


# Вход
# До получаване на командата "Stop" се чете по един ред:
# •	Име на играча с дължина n - текст
# За всеки играч се четат n на брой реда:
# •	число – цяло число в интервала[0…127]

player_name = input()
best_score = 0
best_player = ''
while player_name != "Stop":
    sum = 0  # Важно да е в цикала!!!

    for latter in player_name:
        number = int(input())

        if number == ord(latter):
            sum += 10
        elif number != ord(latter):
            sum += 2

    if sum >= best_score:
        best_score = sum
        best_player = player_name
        sum = 0

    player_name = input()

print(f"The winner is {best_player} with {best_score} points!")
#


#
