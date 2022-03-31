# 1.	Съдомиялна
# Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
# Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от препарат
# за съдомиялна е достатъчно, за да измие определено количество съдове. Знае се, че всяка бутилка съдържа 750 мл.
# препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.  Приемете, че на всяко трето зареждане със съдове,
# съдомиялната се пълни само с тенджери, а останалите пъти с чинии. Докато не получите команда "End"
# ще продължите да получавате бройка съдове, които трябва да бъдат измити.
# Вход
# От конзолата се четат:
# •	Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
# На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи, брой съдове,
# които трябва да бъдат измити - цяло число в интервала [1…100]


number_of_bottles = int(input())
command = input()
count = 1
pots = 0
plates = 0
preparation = number_of_bottles * 750
while command != "End":

    vessels = int(command)

    if count % 3 == 0:
        preparation -= vessels * 15
        pots += vessels

    else:
        plates += vessels
        preparation -= vessels * 5


    if preparation < 0:
        print(f'Not enough detergent, {abs(preparation)} ml. more necessary!')
        break
    count += 1
    command = input()

else:
    print(f'Detergent was enough!')
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {abs(preparation)} ml.')




