# Задача 6. Великденски конкурс
# Напишете програма, която да намира сладкаря с най-висок резултат. В началото на конкурса се въвежда броя на козунаците,
# които ще бъдат дегустирани от посетителите на пекарната, като за всеки козунак различен брой посетители,
# ще дадат оценка от 1 до 10.
# Вход
# Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
# След това за всеки козунак се прочита:
# •	Името на пекаря, който е направил козунака – текст
# •	До получаване на командата "Stop" се прочита
# o	оценка за козунак от един човек  – цяло число в интервала [1... 10]


numbers_of_easter_bread = int(input())

max_point = 0
max_chef = ''
for i in range(numbers_of_easter_bread):
    chef_name = input()
    evaluation = input()

    sum_evaluation = 0
    while evaluation != "Stop":
        sum_evaluation += int(evaluation)
        evaluation = input()

    print(f"{chef_name} has {sum_evaluation} points.")
    if sum_evaluation > max_point:
        max_point = sum_evaluation
        max_chef = chef_name
        print(f"{max_chef} is the new number 1!")

print(f"{max_chef} won competition with {max_point} points!")
# Изход
# След получаване на командата "Stop" се печата един ред:
# •	"{името на пекаря} has {общият брой получени точки} points."
# Ако след командата "Stop", пекарят е с най-много точки до момента, да се отпечата допълнителен ред:
# •	"{името на пекаря} is the new number 1!"
# След дегустация на всички козунаци, да се отпечата един ред:
# •	"{името на пекаря с най-много точки} won competition with {точките на пекаря} points!"
