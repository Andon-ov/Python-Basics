number = int(input())
even_sum = 0
odd_sum = 0
for num in range(number):
    current_number = int(input())
    if num % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
if odd_sum == even_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print(f'No')
    print(f'Diff = {diff}')