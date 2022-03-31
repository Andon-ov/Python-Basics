import sys

n = int(input())
max_number = -sys.maxsize
total = 0

for _ in range(n):
    all_numbers = int(input())
    if all_numbers > max_number:
        max_number = all_numbers
    total += all_numbers
sum = total - max_number
if max_number == sum:
    print("Yes")
    print(f"Sum = {max_number} ")
else:
    diff = abs(max_number - sum)
    print("No")
    print(f"Diff = {diff}")