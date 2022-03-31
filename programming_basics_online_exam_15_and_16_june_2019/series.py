# Задача 5. Сериали
# Разполагате с бюджет и брой сериали, които потребителят ще желае да закупи.
# Всеки сериал съответно има заглавие и цена.
# Някои от сериалите имат намаление:

# •	Thrones – 50%
# •	Lucifer – 40%
# •	Protector – 30%
# •	TotalDrama – 20%
# •	Area – 10%
# Вход


# От конзолата се четат:
# •	Бюджет  - реално  число в интервала [10.0… 100.0]
# •	Брой сериали - n - цяло положително число в интервала [1… 10]
# За всеки сериал се четат по два реда:
# o	Име на сериал - текст
# o	Цена за сериал -  реално  число в интервала [1.0… 15.0]

budget = float(input())
n = int(input())
have_a_money = True
for i in range(n):

	serial_name = input()
	serial_price = float(input())

	# if budget < 0:
	# 	have_a_money = False
	# 	break

	if serial_name == 'Thrones':
		serial_price *= 0.50
		budget -= serial_price
	elif serial_name == 'Lucifer':
		serial_price *= 0.60
		budget -= serial_price
	elif serial_name == 'Protector':
		serial_price *= 0.70
		budget -= serial_price
	elif serial_name == 'TotalDrama':
		serial_price *= 0.80
		budget -= serial_price
	elif serial_name == 'Area':
		serial_price *= 0.90
		budget -= serial_price
	else:
		budget -= serial_price

	if i == (n - 1) and budget < 0:
		have_a_money = False
		break


if not have_a_money:
	print(f"You need {abs(budget):.2f} lv. more to buy the series!")
else:
	print(f"You bought all the series and left with {abs(budget):.2f} lv.")



