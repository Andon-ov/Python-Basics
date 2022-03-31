# •	Брой пакети химикали - цяло число в интервала [0...100]
number_of_packages_of_pens = int(input())
# •	Брой пакети маркери - цяло число в интервала [0...100]
number_of_marketing_packages = int(input())
# •	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
board_cleaners = int(input())
# •	Процент намаление - цяло число в интервала [0...100]
percentage_reduction = int(input())

# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)

price_for_pens = number_of_packages_of_pens * 5.80
price_for_markers = number_of_marketing_packages * 7.20
price_for_cleaners = board_cleaners * 1.20
percentage_reduction /= 100
needed_sum = (price_for_pens + price_for_markers + price_for_cleaners)
total = needed_sum - (needed_sum * percentage_reduction)
print(total)