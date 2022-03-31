# Напишете програма, която до получаване на командата "Stop", чете цели числа,
# въведени от потребителя,  намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.


# while numbers != "Stop":
#     max_number += int(numbers)
#     numbers = input()
#     else:
#         break
# print(max_number)

import sys
max_number = -sys.maxsize

while True:
    numbers = input()
    if numbers == "Stop":
        break

    elif int(numbers) > max_number:
        max_number = int(numbers)


print(max_number)