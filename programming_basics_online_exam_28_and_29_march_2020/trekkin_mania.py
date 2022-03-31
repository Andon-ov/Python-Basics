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