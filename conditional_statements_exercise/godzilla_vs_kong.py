budget = float(input())
number_of_statist = int(input())
one_dress_price = float(input())
decore = budget * 0.1
dress_price = number_of_statist * one_dress_price
if number_of_statist > 150:
    dress_price *= 0.9
needed_money = decore + dress_price
differance = abs(needed_money - budget)
if needed_money > budget:
    print('Not enough money!')
    print(f'Wingard needs {differance:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {differance:.2f} leva left.')