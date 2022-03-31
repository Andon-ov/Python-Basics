# start_number = input()
# end_number = input()
# n_1 = 0
# n_2 = 0
# n_3 = 0
# n_4 = 0
# e_1 = 0
# e_2 = 0
# e_3 = 0
# e_4 = 0
# for x, number in enumerate(start_number):
#     if x == 0:
#         n_1 = int(number)
#     elif x == 1:
#         n_2 = int(number)
#     elif x == 2:
#         n_3 = int(number)
#     else:
#         n_4 = int(number)
#
# for y, number_end in enumerate(end_number):
#     if y == 0:
#         e_1 = int(number_end)
#     elif y == 1:
#         e_2 = int(number_end)
#     elif y == 2:
#         e_3 = int(number_end)
#     else:
#         e_4 = int(number_end)
# for a in range(n_1, e_1 + 1):
#     for b in range(n_2, e_2 + 1):
#         for c in range(n_3, e_3 + 1):
#             for d in range(n_4, e_4 + 1):
#                 if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
#                     print(f'{a}{b}{c}{d}', end=' ')



first_number = input()
second_number = input()

for a in range(int(first_number[0]),int(second_number[0]) + 1):
    for b in range(int(first_number[1]),int(second_number[1]) + 1):
        for c in range(int(first_number[2]),int(second_number[2]) + 1):
            for d in range(int(first_number[3]),int(second_number[3]) + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f'{a}{b}{c}{d}', end=' ')
