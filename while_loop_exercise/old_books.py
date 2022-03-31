 # Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст).
# Докато Ани не намери любимата си книга
 # или не провери всички книги в библиотеката,
# програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст),
# която тя проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".

wanted_book = input()
is_book_found = False
count = 0
book = input()
while book != "No More Books":
    if book == wanted_book:
        is_book_found = True
        break
    count += 1
    book = input()

# •	Ако открие книгата си се отпечатва един ред:
if is_book_found:
    print(f"You checked {count} books and found it.")

# •	Ако не открие търсената книгата да се отпечата на два реда:

else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")


