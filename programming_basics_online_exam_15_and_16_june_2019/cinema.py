# Задача 4. Кино
# Получавате места в залата и на всеки следващ ред до команда "Movie time!",
# колко хора влизат в залата. Цената на един билет е 5 лв. Ако текущия брой хора влезли в залата се дели на 3 без остатък,
# се прави отстъпка 5лв от общата им сметка.

# Ако в залата се опитат да влязат повече хора от колкото места са останали, то се счита че местата са изчерпани и
# програмата трябва да приключи четенето на вход.


# От конзолата се четат:
# •	На първия ред - капацитет на залата - цяло число в интервала [50... 150]
# На всеки следващ ред до команда "Movie time!":
# o	Брой хора влизащи в киното - цяло число в интервала [1… 15]

capacity_of_hall = int(input())
command = input()
the_hall_is_full = False
sum = 0
sum_number_of_people = 0
while command != "Movie time!":



	number_of_people = int(command)
	sum_number_of_people += number_of_people

	if sum_number_of_people > capacity_of_hall:
		the_hall_is_full = True
		break

	if number_of_people % 3 ==0:


		sum += (number_of_people * 5) - 5
	else:

		sum += (number_of_people * 5)

	if sum_number_of_people > capacity_of_hall:
		the_hall_is_full = True
		break

	command = input()
else:
	print(f"There are {capacity_of_hall - sum_number_of_people} seats left in the cinema.")

if the_hall_is_full:
	print(f"The cinema is full.")
print(f"Cinema income - {sum} lv.")

# Изход
# На конзолата първо да се отпечата един ред:
# •	При получена команда "Movie time!":
#  "There are {останали места} seats left in the cinema."
# •	При изчерпване на местата в залата:
# 	"The cinema is full."
# След това да се отпечата:
# 	"Cinema income - {приходи от залата} lv."
