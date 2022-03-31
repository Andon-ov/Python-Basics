# Задача 5. Фитнес център
# Напишете програма, която да изчислява броя на посетителите в един фитнес център.
# В началото програмата получава броя на посетителите на фитнеса и за всеки човек - дейността,
# която извършва във фитнеса. На края програмата трябва да отпечата броят трениращи за всяка една дейност
# ("Back", "Chest", 'Legs", "Abs") и броят клиенти, закупили продукт ("Protein shake", "Protein bar"). '
# Също така - процентът трениращи (спрямо общия брой посетители) и процентът на клиентите, закупили продукт от фитнеса.
# Вход
# От конзолата се чете число, след това поредица от низове, всяко на отделен ред:
# •	На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
# •	За всеки един посетител на отделен ред – дейността във фитнеса – текст
# ("Back", "Chest", "Legs", "Abs", "Protein shake" или "Protein bar")

people_in_fitness = int(input())
back = 0
chest = 0
legs = 0
abs_training = 0
protein_shake = 0
protein_bar = 0

for i in range(people_in_fitness):
    what_do_they_want = input()
    if what_do_they_want == "Back":
        back += 1
    elif what_do_they_want == "Chest":
        chest += 1
    elif what_do_they_want == "Legs":
        legs += 1
    elif what_do_they_want == "Abs":
        abs_training += 1
    elif what_do_they_want == "Protein shake":
        protein_shake += 1
    elif what_do_they_want == "Protein bar":
        protein_bar += 1


print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_training} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(((back + chest + legs + abs_training)*100)/people_in_fitness):.2f}% - work out")
print(f"{(((protein_shake + protein_bar)*100)/people_in_fitness):.2f}% - protein")
# Всички проценти трябва да са форматирани до втората цифра след десетичния знак.
