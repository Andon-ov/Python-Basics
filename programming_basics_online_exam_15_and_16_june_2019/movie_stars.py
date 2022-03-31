# Ако името на актьора е по-дълго от 15 символа възнаграждението му ще е 20 % от останалия бюджет до момента.
# Ако бюджета в даден момент свърши, програмата трябва да прекъсне.

# От конзолата първо се чете един ред:
# •	Бюджет за актьори - реално число в интервала [1000.0... 2 100 000.0]
# След това се четат многократно по един или два реда до команда "ACTION" или до изчерпване на бюджета:
# •	Име на актьор - текст
# Ако името на актьора съдържа по-малко или равно на 15 брой символи:
# o	Възнаграждение - реално число в интервала [250.0… 1 000 000.0]
money_we_have = float(input())
command = str(input())
money_we_have_finish = False
while command != "ACTION":


    if len(command) <= 15:
        bugget = float(input())
        money_we_have -= bugget
    else:
        money_we_have *= 0.80


    command = str(input())

    if money_we_have < 0:
        money_we_have_finish = True
        break

if money_we_have_finish:
    print(f"We need {abs(money_we_have):.2f} leva for our actors.")
if not money_we_have_finish:
    print(f"We are left with {abs(money_we_have):.2f} leva.")



# На конзолата да се отпечата един ред:
# •	Ако бюджета е достатъчен :
# print(f"We are left with {abs(money_we_have)} leva.")
# •	Ако бюджета не е достатъчен:
# print(f"We need {abs(money_we_have)} leva for our actors.")
# Резултата да се форматира до втората цифра след десетичния знак!
