# 12.	Търговски комисионни
# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Град	0 ≤ s ≤ 500	  500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
# Sofia	      5%	        7%	              8%	           12%
# Varna	      4.5%	        7.5%	         10%	           13%
# Plovdiv	  5.5%	          8%	          12%	           14.5%
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".
town = input()
sales_volume = float(input())
commission = 0
condition = True
if town == 'Sofia':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.05
    elif 500 <= sales_volume <= 1000:
        commission = sales_volume * 0.07
    elif 1000 <= sales_volume <= 10000:
        commission = sales_volume * 0.08
    elif sales_volume > 10000:
        commission = sales_volume * 0.12
    else:
        condition = False

elif town == 'Varna':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.045
    elif 500 <= sales_volume <= 1000:
        commission = sales_volume * 0.075
    elif 1000 <= sales_volume <= 10000:
        commission = sales_volume * 0.10
    elif sales_volume > 10000:
        commission = sales_volume * 0.13
    else:
        condition = False

elif town == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.055
    elif 500 <= sales_volume <= 1000:
        commission = sales_volume * 0.08
    elif 1000 <= sales_volume <= 10000:
        commission = sales_volume * 0.12
    elif sales_volume > 10000:
        commission = sales_volume * 0.145
    else:
        condition = False
else:
    condition = False
if condition:
    print(f'{commission:.2f}')
else:
    print('error')