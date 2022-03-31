# Задача 1. Оборудване за тенис

import math

price_of_tennis_racket = float(input())
tennis_rackets = int(input())
number_of_sneakers = int(input())
sneakers_price = price_of_tennis_racket * 0.1666666666666667

other_thinks = ((price_of_tennis_racket * tennis_rackets) + (number_of_sneakers * sneakers_price)) * 0.20
total = (price_of_tennis_racket * tennis_rackets) + (number_of_sneakers * sneakers_price) + other_thinks

print(f"Price to be paid by Djokovic {math.floor(total / 8)}")
print(f"Price to be paid by sponsors {math.ceil(total / 1.14285714286)}")
