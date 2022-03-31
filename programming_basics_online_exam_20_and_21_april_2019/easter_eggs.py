# Предстои Великден и едно от най-вълнуващите неща е боядисването на яйца. Наличните цветове за боядисване са:
# •	червено (red)
# •	оранжев (orange)
# •	син (blue)
# •	зелен (green)
# Напишете програма, която изчислява какъв е броят на яйцата от всеки цвят и от кой цвят яйцата са най - много,
# като знаете общия им брой и цвета на всяко яйце.
# Вход
# От конзолата се чете 1 ред:
# •	 Броят на боядисаните яйца – цяло число в интервала [1 ... 100]
# За всяко яйце се чете:
# o	Цветът на яйцето – текст с възможности: "red", "orange", "blue", "green"
painted_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
max_egg = 0
max_color = ''
for i in range(painted_eggs):
    egg_color = input()
    if egg_color == "red":
        red += 1
        if red > max_egg:
            max_egg = red
            max_color = "red"
    elif egg_color == "orange":
        orange += 1
        if orange > max_egg:
            max_egg = orange
            max_color = "orange"
    elif egg_color == "blue":
        blue += 1
        if blue > max_egg:
            max_egg = blue
            max_color = "blue"
    elif egg_color == "green":
        green += 1
        if green > max_egg:
            max_egg = green
            max_color = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_egg} -> {max_color}")
