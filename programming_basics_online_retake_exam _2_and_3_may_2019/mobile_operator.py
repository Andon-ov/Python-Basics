# Мобилен оператор предлага договори с различна месечна такса в зависимост от срока - 1 или 2 години. Да се
# напише програма, която изчислява дължимата сума, която трябва да се плати за определен брой месеци.
# срок / тип        Small       Middle      Large       ExtraLarge
# 1 година(one)     9.98 лв.    18.99 лв.   25.98 лв.   35.99 лв.
# 2 години(two)     8.58 лв.    17.09 лв.   23.59 лв.   31.79 лв.
# Условия:

# Вход
# От конзолата се четат 3 реда:
# 1. Срок на договор – текст – "one", или "two"
# 2. Тип на договор – текст – "Small", "Middle", "Large"или "ExtraLarge"
# 3. Добавен мобилен интернет – текст – "yes" или "no"
# 4. Брой месеци за плащане - цяло число в интервала [1 … 24]

duration_of_contract = input()
type_of_contract = input()
added_mobile_internet = input()
number_of_months_to_pay = int(input())
tax = 0
price = 0

if duration_of_contract == "one":

    if type_of_contract == "Small":
        tax = 9.98
    elif type_of_contract == "Middle":
        tax = 18.99
    elif type_of_contract == "Large":
        tax = 25.98
    elif type_of_contract == "ExtraLarge":
        tax = 35.99

elif duration_of_contract == "two":

    if type_of_contract == "Small":
        tax =  8.58
    elif type_of_contract == "Middle":
        tax =  17.09
    elif type_of_contract == "Large":
        tax =  23.59
    elif type_of_contract == "ExtraLarge":
        tax =  31.79


if added_mobile_internet == "yes" :
    if tax <= 10:
        tax += 5.50
    elif tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85
price = tax * number_of_months_to_pay
if duration_of_contract == "two":
    price *= 0.9625

print(f"{price:.2f} lv.")

#  при добавен мобилен интернет, към таксата за един месец се добавя:
# o при такса по-малка или равна на 10.00 лв.  5.50 лв.
# o при такса по-малка или равна на 30.00 лв.  4.35 лв.
# o при такса по-голяма от 30.00 лв.  3.85 лв.
#  ако договорът e за две години, общата сума се намалява с 3.75%





#  Цената, която заплаща клиентът, форматирана до втория знак след десетичната запетая, в следния
