# 11.	Магазин за плодове
# Магазин за плодове през работните дни работи на следните цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	0.85	1.45	2.70	5.50	3.85
# През събота и неделя магазинът работи на по-високи цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	1.25	0.90	1.60	3.00	5.60	4.20
# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя,
# и пресмята цената според цените от таблиците по-горе:
# •	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# •	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# •	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".
fruit = input()
day_of_week = input()
quantity = float(input())
sum = 0
condition = True
if day_of_week in 'Monday'  'Tuesday'  'Wednesday'  'Thursday'  'Friday':
    if fruit == 'banana':
        sum = quantity * 2.5
    elif fruit == 'apple':
        sum = quantity * 1.2
    elif fruit == 'orange':
        sum = quantity * 0.85
    elif fruit == 'grapefruit':
        sum = quantity * 1.45
    elif fruit == 'kiwi':
        sum = quantity * 2.7
    elif fruit == 'pineapple':
        sum = quantity * 5.5
    elif fruit == 'grapes':
        sum = quantity * 3.85
    else:
        condition = False
# цена	2.70	1.25	0.90	1.60	3.00	5.60	4.20
# banana	apple	orange	grapefruit	kiwi	pineapple	grapes
elif day_of_week in 'Saturday'  'Sunday':
    if fruit == 'banana':
        sum = quantity * 2.7
    elif fruit == 'apple':
        sum = quantity * 1.25
    elif fruit == 'orange':
        sum = quantity * 0.90
    elif fruit == 'grapefruit':
        sum = quantity * 1.60
    elif fruit == 'kiwi':
        sum = quantity * 3
    elif fruit == 'pineapple':
        sum = quantity * 5.6
    elif fruit == 'grapes':
        sum = quantity * 4.2
    else:
        condition = False

else:
    condition = False
if condition:
    print(f'{sum:.2f}')
else:
    print('error')