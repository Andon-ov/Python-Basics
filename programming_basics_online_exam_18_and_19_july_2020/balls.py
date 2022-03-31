
#  Ако топката е “red” точките ни се повишават с 5.
#  Ако топката е “orange” точките ни се повишават с 10.
#  Ако топката е “yellow” точките ни се повишават с 15.
#  Ако топката е “white” точките ни се повишават с 20.
#  Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.
import math

n = int(input())
total_point = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
black_ball = 0 #(колко пъти делим на 2)
for _ in range(n):
    n_colors = input()
    if n_colors == 'red':
        total_point += 5
        red_balls += 1

    elif n_colors == 'orange':
        total_point += 10
        orange_balls += 1

    elif n_colors == 'yellow':
        total_point += 15
        yellow_balls += 1

    elif n_colors == 'white':
        total_point += 20
        white_balls += 1

    elif n_colors == 'black':
        total_point /= 2
        black_ball += 1

    else:
        other_balls += 1

print(f'Total points: {math.floor(total_point)}')
print(f'Points from red balls: {red_balls}')
print(f'Points from orange balls: {orange_balls}')
print(f'Points from yellow balls: {yellow_balls}')
print(f'Points from white balls: {white_balls}')
print(f'Other colors picked: {other_balls}')
print(f'Divides from black balls: {black_ball}')




