# Задача 3. Билети за снукър
# да напишете програма за продаване на билети, като се има предвид следния ценоразпис:
# 				Четвъртфинал	Полуфинал		Финал
# Стандартен	55.50 £/бр.		75.88 £/бр.		110.10 £/бр.
# Премиум		105.20 £/бр.	125.22 £/бр.	160.66 £/бр.
# ВИП			118.90 £/бр.	300.40 £/бр.	400 £/бр.

# При закупуване на билет, зрителят може да избере опция, снимка с трофея, на цена 40 лири.
# При достигане на определена сума има отстъпки:
# •	Над 4000 лири има 25% отстъпка и безплатни снимки с трофея (ако  опцията за снимки е избрана,
#  таксата от 40 лири за билет не се включва)
# •	Над 2500 лири има 10% отстъпка
# При избрана опция за снимки с трофея, цената се начислява след изчисляването на отстъпките.

# Вход
# От конзолата се четат 3 реда:
# 1.	Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
# 2.	Вид на билета – текст - “Standard”, “Premium” или “VIP”
# 3.	Брой билети – цяло число в интервала [1 … 30]
# 4.	Снимка с трофея – символ – 'Y' (да) или 'N' (не)

championship_stage = input()
type_of_ticket = input()
number_of_tickets = int(input())
photo_with_trophy = input()
price = 0
final_price = 0
more_than_4000 = False
if championship_stage == 'Quarter final':
	if type_of_ticket == 'Standard':
		price += 55.50
	elif type_of_ticket == 'Premium':
		price += 105.20
	elif type_of_ticket == 'VIP':
		price += 118.90
elif championship_stage == 'Semi final':
	if type_of_ticket == 'Standard':
		price += 75.88
	elif type_of_ticket == 'Premium':
		price += 125.22
	elif type_of_ticket == 'VIP':
		price += 300.40
elif championship_stage == 'Final':
	if type_of_ticket == 'Standard':
		price += 110.10
	elif type_of_ticket == 'Premium':
		price += 160.66
	elif type_of_ticket == 'VIP':
		price += 400

final_price = price * number_of_tickets


if final_price > 4000:
	final_price *= 0.75
	more_than_4000 = True

elif final_price > 2500:
	final_price *= 0.90

if photo_with_trophy == 'Y' and not more_than_4000:
	final_price += 40 * number_of_tickets

print(F'{final_price:.2f}')

