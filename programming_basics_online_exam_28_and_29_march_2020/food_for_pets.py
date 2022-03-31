# Всеки ден кучето и котката изяждат различно количество отобщата им храна.
# На всеки трети ден получават награда - бисквитки. Количеството на бисквитките е 10% от
# общо изядената храна за деня.
# Вашата програма трябва да отпечатва статистика за количеството бисквитки, които са изяли, колко процента
# от първоначалното количество обща храна са изяли и колко процента от изядената храна е изяло кучето и
# колко е изяла котката.
# Вход
# Първоначално се чете един ред:
#  Брой дни – цяло число в диапазона [1…30]
#  Общо количество храна – реално число в диапазона [0.00…10000.00]
# След това за всеки ден се чете:
# o Количество изядена храна от кучето – цяло число в диапазона [10…500]
# o Количество изядена храна от котката – цяло число в диапазона [10…500]


number_of_days = int(input())
total_amount_of_food = float(input())
dog_food = 0
cat_food = 0
biscuits = 0

for day in range(1, number_of_days +1):

    amount_food_dog = int(input())
    amount_food_cat = int(input())

    dog_food += amount_food_dog
    cat_food += amount_food_cat

    if day % 3 == 0:
        biscuits += (amount_food_cat + amount_food_dog) * 0.10

total_food = dog_food + cat_food
percentage_of_food_eaten = ((total_food) / total_amount_of_food) * 100
percentage_of_food_eaten_dog = ( dog_food / (total_food)) * 100
percentage_of_food_eaten_cat = ( cat_food / (total_food)) * 100


print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percentage_of_food_eaten:.2f}% of the food has been eaten.")
print(f"{percentage_of_food_eaten_dog:.2f}% eaten from the dog.")
print(f"{percentage_of_food_eaten_cat:.2f}% eaten from the cat.")

