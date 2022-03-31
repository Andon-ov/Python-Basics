n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(n):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    elif current_number >= 800:
        p5 += 1
total_p1 = p1/ n * 100
total_p2 = p2/ n * 100
total_p3 = p3/ n * 100
total_p4 = p4/ n * 100
total_p5 = p5/ n * 100
print(f'{total_p1:.2f}%')
print(f'{total_p2:.2f}%')
print(f'{total_p3:.2f}%')
print(f'{total_p4:.2f}%')
print(f'{total_p5:.2f}%')