# 8.	Еднакви двойки
# Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н.
# Всяка двойка има стойност – сумата от съставящите я числа. Напишете програма, която проверява дали всички двойки имат
# еднаква стойност или печата максималната разлика между две последователни двойки. Ако всички двойки имат еднаква
# стойност, отпечатайте "Yes, value = {Value}" + стойността. В противен случай отпечатайте "No, maxdiff = {Difference}"
# + максималната разлика.
import sys

n = int(input())
all_sum = 0
max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(n):

    number = int(input())
    number1 = int(input())
    sum = number + number1

    if sum > max_number:
        max_number = sum
    if sum < min_number:
        min_number = sum

    all_sum += number + number1

if min_number == max_number:
    print(f"Yes, value={int(all_sum / n)}")
else:
    print(f"No, maxdiff={(max_number - min_number)}")





# ToDO 87 / 100 - да си намеря грешката - долното работи
# https://judge.softuni.org/Contests/Practice/Index/1680#7

numbers = int(input())
previous_number = 0
max_difference = 0

for num in range(numbers):
    first_number = int(input())
    second_number = int(input())

    if num > 0:
        if abs(previous_number - first_number - second_number) > max_difference:
            max_difference = abs(previous_number - first_number - second_number)

    previous_number = first_number + second_number

if max_difference == 0:
    print(f"Yes, value={previous_number}")
else:
    print(f"No, maxdiff={max_difference}")