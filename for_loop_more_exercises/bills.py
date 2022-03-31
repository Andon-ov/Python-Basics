# 6.	Месечни разходи
# Напишете програма която да пресмята средният разход за месец на семейство за даден период време.
# За всеки месец разходите са следните:
# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.
# Вход
# Входът се чете от конзолата:
# •	Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
# •	За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]
month = int(input())
electricity_bill = 0
for i in range(month):
    electricity = float(input())
    electricity_bill += electricity
    water = month * 20
    net = month * 15
    other = ((net + water + electricity_bill) * 1.2)
    total = (water + net +electricity_bill +other) / month

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {net:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {total:.2f} lv")
# Всички числа трябва да са форматирана до вторият знак след запетаята.