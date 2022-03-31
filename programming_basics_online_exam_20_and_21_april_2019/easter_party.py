# Задача 2.  Великденско парти
# Ако покани:
# •	Между 10 (вкл.) и 15 (вкл.) човека -> 15 % отстъпка от куверта за един човек
# •	Между 15 и 20 (вкл.) човека -> 20 % отстъпка от куверта за един човек
# •	Над 20 човека -> 25 % отстъпка от куверта за един човек
# Деси трябва да предвиди и закупуването на торта за партито. Цената на тортата е 10% от бюджета на Деси.
# Напишете програма, която изчислява дали бюджетът на Деси ще и е достатъчен за партито.
# Вход
number_of_guests = int(input())
price_for_one_person = float(input())
desi_budget = float(input())
cake = desi_budget * 0.10
if 10 <= number_of_guests <= 15:
    price_for_one_person *= 0.85
elif 15< number_of_guests <= 20:
    price_for_one_person *= 0.80
elif number_of_guests > 20:
    price_for_one_person *= 0.75

total_price = (number_of_guests * price_for_one_person) + cake
final_sum = abs(total_price - desi_budget)
if desi_budget >= total_price:

    print(f"It is party time! {final_sum:.2f} leva left.")
else:
    print(f"No party! {final_sum:.2f} leva needed.")

# Изход
# На конзолата да се отпечата един ред:
# •	Ако бюджетът  е достатъчен:
# o	"It is party time! {останали пари} leva left."
# •	Ако бюджетът не е достатъчен:
# o	"No party! {недостигащи пари} leva needed."
# Резултатът да бъде форматиран до втория знак след десетичната запетая.
