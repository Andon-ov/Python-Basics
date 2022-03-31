# username = input()
# password = input()
#
# entered_password = input()
# while entered_password != password:
#     entered_password = input()
# print(f'Welcome {username}!')


username = input()
password = input()
found_password = input()
while True:
    if found_password == password:
        print(f'Welcome {username}!')
        break

    else:
        found_password = input()



