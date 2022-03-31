# 1.	Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
# 2.	Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# 3.	Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
# 4.	Дни за престой - цяло число в интервала [1 … 10000]


city = input()
type_of_package = input()
vip = input()
days_to_stay = int(input())
sum = 0
true = True
if days_to_stay < 1:
    true = False
    print(f'Days must be positive number!')
elif city not in("Bansko" "Borovets" "Varna" "Burgas") or type_of_package not in("noEquipment" "withEquipment" 
                                                                                  "noBreakfast" "withBreakfast"):
    true = False
    print(f"Invalid input!")

if days_to_stay > 7:
    days_to_stay -= 1

if city in("Bansko" "Borovets"):
    if type_of_package == "withEquipment":
        sum += days_to_stay * 100
        if vip == "yes":
            sum *= 0.90
    elif type_of_package == "noEquipment":
        sum += days_to_stay * 80
        if vip == "yes":
            sum *= 0.95
elif city in("Varna" "Burgas"):
    if type_of_package == "withBreakfast":
        sum += days_to_stay * 130
        if vip == "yes":
            sum *= 0.88
    elif type_of_package == "noBreakfast":
        sum += days_to_stay * 100
        if vip == "yes":
            sum *= 0.93
if true:
    print(f"The price is {sum:.2f}lv! Have a nice time!")






# Ако клиентът е заявил престой повече от 7 дни, получава единия ден безплатно.
# Изход
# На конзолата се отпечатва 1 ред:
# •	Когато потребителят е въвел всички данни правилно, отпечатваме:
# "The price is {цената, форматирана до втория знак}lv! Have a nice time!"
# •	Ако потребителят е въвел по-малко от 1 ден за престой, отпечатваме:
# "Days must be positive number!"
# •	Когато при въвеждането на града или вида на пакета се въведат невалидни данни, отпечатваме: "Invalid input!"
# #