# 4.	Стъпки

# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
# Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато
# постигне целта си да се изписва "Goal reached! Good job!"

# и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
# които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си,
# на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."

# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
target_steps = 10000
total_steps = 0

while total_steps < target_steps:        # цикълът винаги върти на обратното на това което търсим!!!

    command = input()
    if command == "Going home":          # ако получим команда, че си отива пак имаме вход за последни стъпки.
        last_steps = int(input())
        total_steps += last_steps
        break
    current_steps = int(command)
    total_steps += current_steps

diff = abs(target_steps - total_steps)
if total_steps >= target_steps:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

else:
    print(f'{diff} more steps to reach goal.')