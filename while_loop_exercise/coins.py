# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с
# колко най-малко монети може да стане това.
# sum = float(input())
# sum = int(sum * 100)
# coin_counter = 0
# # while sum > 0:
# #     if sum - 200 >= 0:
#         coin_counter += 1
#         sum -= 200
#         continue
#     elif sum - 100 >= 0:
#         coin_counter += 1
#         sum -= 100
#         continue
#     elif sum - 50 >= 0:
#         coin_counter += 1
#         sum -= 50
#         continue
#     elif sum - 20 >= 0:
#         coin_counter += 1
#         sum -= 20
#         continue
#     elif sum - 10 >= 0:
#         coin_counter += 1
#         sum -= 10
#         continue
#     elif sum - 5 >= 0:
#         coin_counter += 1
#         sum -= 5
#         continue
#     elif sum - 2 >= 0:
#         coin_counter += 1
#         sum -= 2
#         continue
#     elif sum - 1 >= 0:
#         coin_counter += 1
#         sum -= 1
# print(coin_counter)

sum = float(input())
sum = int(sum * 100)
coin_counter = 0
coin_counter += sum // 200
sum %= 200
coin_counter += sum // 100
sum %= 100
coin_counter += sum // 50
sum %= 50
coin_counter += sum // 20
sum %= 20
coin_counter += sum // 10
sum %= 10
coin_counter += sum // 5
sum %= 5
coin_counter += sum // 2
sum %= 2
coin_counter += sum // 1
sum %= 1

print(coin_counter)
