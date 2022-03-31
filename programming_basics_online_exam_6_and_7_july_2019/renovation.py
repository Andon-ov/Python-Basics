# Задача 4. Ремонт
# Пешо решава, че иска да направи ремонт вкъщи. Неговата задача е да боядиса стените в хола,
# като знаете височината и ширината на една стена. Холът на Пешо има 4 стени с еднакви размери,
# определен процент от които се заемат от прозорци и врати, които няма да бъдат боядисвани.
# Той не е сигурен дали ще успее наведнъж, затова моли Вас да му помогнете да изчисли дали ще му остава още
# работа за следващия ден и, ако да, колко кв. м. има да довърши, а в случай, че успее да боядиса хола,
# колко боя му е останала (трябва да се има предвид, че с един литър боя се боядисва един квадратен метър от стената).
# Вход
# От конзолата се четат следните редове:
# 1.	Височина на стената - цяло число [0… 100]
# 2.	Ширина на стената - цяло число [0… 100]
# 3.	Процент от общата площ на стените, който няма да бъде боядисан - цяло число [5… 95]

wall_height = int(input())
wall_width = int(input())
total_area_will_not_painted = int(input())
command = input()
total_painted = 0
paint_finish = False
common_surface = (wall_width * wall_height * 4)  - ((wall_width * wall_height * 4) * (total_area_will_not_painted / 100))
while command != "Tired!":
    liters_of_paint = int(command)
    total_painted += liters_of_paint


    if total_painted == common_surface:
        paint_finish = True
        print(f"All walls are painted! Great job, Pesho!")
        break
    elif total_painted > common_surface:
        paint_finish = True
        print(f"All walls are painted and you have {int(abs(common_surface - total_painted))} l paint left!")
        break
    command = input()
if not paint_finish:
    print(f"{int(abs(common_surface - total_painted))} quadratic m left." )
# Забележка: Площта за боядисване да бъде закръглена нагоре до най-близкото цяло число.





# На следващите редове до получаване на командата "Tired!" или докато не бъдат боядисани всички стени,
# се чете по едно число:
# •	Литри боя – цяло число [0…100]:
# Забележка: Площта за боядисване да бъде закръглена нагоре до най-близкото цяло число.
# Изход
# Да се отпечата на конзолата един от следните редове:
# •	При получаване на командата "Tired!":
# "{квадратни метри} quadratic m left."
# {квадратни метри} е повърхнината, която му остава да боядисана.
# •	Aко е останала боя в излишък:
# "All walls are painted and you have {литри боя} l
#  paint left!"
# •	Aко след боядисването на всички стени, не е останала боя:
# "All walls are painted! Great job, Pesho!"
