# 7. Трекинг мания
# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на групата,
# катерачите ще изкачват различни върхове.
# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# •	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до втората цифра
# след десетичната запетая.
# •	Първи ред - процентът изкачващи Мусала
# •	Втори ред – процентът изкачващи Монблан
# •	Трети ред – процентът изкачващи Килиманджаро
# •	Четвърти ред – процентът изкачващи К2
# •	Пети ред – процентът изкачващи Еверест

number_groups_of_climbers = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
all_people = 0

for _ in range(number_groups_of_climbers):
    number_people_in_group = int(input())
    all_people += number_people_in_group
    if number_people_in_group <= 5:
        musala += number_people_in_group
    elif number_people_in_group <= 12:
        mont_blanc += number_people_in_group
    elif number_people_in_group <= 25:
        kilimanjaro += number_people_in_group
    elif number_people_in_group <= 40:
        k2 += number_people_in_group
    elif number_people_in_group >= 41:
        everest += number_people_in_group

musala_total = musala / all_people * 100
mont_blanc_total = mont_blanc / all_people * 100
kilimanjaro_total = kilimanjaro / all_people * 100
k2_total = k2 / all_people * 100
everest_total = everest / all_people * 100

print(f'{musala_total:.2f}%')
print(f'{mont_blanc_total:.2f}%')
print(f'{kilimanjaro_total:.2f}%')
print(f'{k2_total:.2f}%')
print(f'{everest_total:.2f}%')