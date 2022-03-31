floor = int(input())
room = int(input())
room_numbers = ''
for f in range(floor, 0 , -1):
    for r in range(room):
        current_room = f * 10 + r
        if f == floor:
            print(f'L{current_room} ', end='')
        elif f % 2 == 0:
            room_numbers += f'O{current_room} '
        else:
            room_numbers += f'A{current_room} '
    print(room_numbers)
    room_numbers = ''



