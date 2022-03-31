import sys
min_number = sys.maxsize

while True:
    numbers = input()
    if numbers == "Stop":
        break

    elif int(numbers) < min_number:
        min_number = int(numbers)


print(min_number)