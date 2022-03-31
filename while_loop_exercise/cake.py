# 6.	Торта
# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта. Той обаче не знае колко парчета могат
# да си вземат гостите от нея.
# Вашата задача е да напишете програма, която изчислява броя на парчетата, които гостите са взели преди тя да свърши.
# Ще получите размерите на тортата (широчина и дължина –цели числа и след това на всеки ред,
#
# до получаване на командата "STOP" или докато не свърши тортата,
# броят на парчетата, които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# •	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# •	"No more cake left! You need {брой недостигащи парчета} pieces more."
h = int(input())
l = int(input())
pieces_of_cake = h * l
cake_is_over = False
command = input()

while command != 'STOP':
    current_number_of_pieces = int(command)
    pieces_of_cake -= current_number_of_pieces
    if pieces_of_cake <0:
        cake_is_over = True
        break
    command = input()

if cake_is_over:
    print(f'No more cake left! You need {abs(pieces_of_cake)} pieces more.')
else:
    print(f'{abs(pieces_of_cake)} pieces are left.')



