current_sum = 0
while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())

    while budget > current_sum:
        save_sum = float(input())
        current_sum += save_sum

        if current_sum >= budget:
            print(f'Going to {destination}!')
            current_sum = 0
            break
