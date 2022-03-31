# Задача 5. Товарене на багажи
# Всеки самолет има определен капацитет на багажника. До получаване на команда "End" ще получавате обем на куфар.
# Обемът на всеки трети куфар трябва да се увеличава с 10%, поради загубата на пространство при начина на подреждане.
# Ако свободното пространството в даден момент е по-малко от обема на куфар товаренето трябва да прекъсне.
# Вход
# Първоначално се чете един ред:
# •	Капацитетът на багажника – реално число в диапазона [100.0…6000.0]
# След това до получаване на команда "End" или до запълване на багажника, се чете по един ред:
# o	Обем на куфар – реално число в диапазона [100.0…6000.0]

trunk_capacity = float(input())
volume_of_suitcases = input()
volume_count = 0
count = 1
while volume_of_suitcases != "End":
    volume = float(volume_of_suitcases)

    if count % 3 == 0:
        volume *= 1.1


    volume_count += volume

    if trunk_capacity < volume_count:
        print("No more space!")
        break
    volume_of_suitcases = input()
    count += 1

else:
    print(f"Congratulations! All suitcases are loaded!")


print(f"Statistic: {count - 1} suitcases loaded.")











# Изход
# На конзолата да се отпечатат следните редове според случая:
# •	При получаване на командата "End" се печата:
# "Congratulations! All suitcases are loaded!"
# •	Ако обемът на куфара е по-голям от оставащото пространство в багажника:
# "No more space!"
# •	Накрая винаги се отпечатва статистика – колко багажа са натоварени:
# "Statistic: {брой натоварени багажи} suitcases loaded."
