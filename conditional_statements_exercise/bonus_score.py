score = int(input())
bonus_point = 0
if score <= 100:
    bonus_point += 5                        # bonus_point = bonus_point + 5
elif 100 < score <= 1000:
    bonus_point += score * 0.2       # 20 / 100
else:
    bonus_point += score * 0.1       # 10 / 100
if score % 2 == 0:                         # Проверяваме дали числото е четно
    bonus_point += 1
if score % 10 == 5:                        # Проверяваме дали числото завършва на 5
    bonus_point += 2
print(bonus_point)
print(bonus_point + score)