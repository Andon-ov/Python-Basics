first_time = int(input())
second_time = int(input())
third_time = int(input())
totall_time = first_time + second_time + third_time
# Използваме цялочислено деление (което ни показва минутите) //
min = totall_time // 60
# Използваме модулно деление(което ни показва остатакът) %
sec = totall_time % 60
# Искаме да започват секундите с 0 тоест добавяме нула на числата 0-9
# Може и така без проверка ... print(f'{min}:{sec:02d}') и така print(f'{min}:{sec:0>2d}')
if sec < 10:
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')