# # 3.	Логистика
# # Отговаряте за логистиката на различни товари. В зависимост от теглото на товара е нужно различно превозно средство.
# # Цената на тон, за която се превозва товара е различна за всяко превозно средство:
#
# # Вашата задача е да изчислите средната цена на тон превозен товар,
# # както и процента на тоновете  превозвани с всяко превозно средство, спрямо общото тегло(в тонове) на всички товари.


number_of_goods_to_be_transported = int(input())
minibus = 0
truck = 0
train = 0
minibus_load = 0
truck_load = 0
train_load = 0
all_loads = 0

for i in range(number_of_goods_to_be_transported):
    goods_in_tons = int(input())
    if goods_in_tons <= 3:
        all_loads += goods_in_tons
        minibus += (goods_in_tons * 200)
        minibus_load += goods_in_tons

    elif goods_in_tons <= 11:
        all_loads += goods_in_tons
        truck += (goods_in_tons * 175)
        truck_load += goods_in_tons

    elif goods_in_tons >= 12:
        all_loads += goods_in_tons
        train += (goods_in_tons * 120)
        train_load += goods_in_tons

average_price_per_tonne = minibus + truck + train

print(f'{(average_price_per_tonne / all_loads):.2f}')
print(f'{((minibus_load/all_loads)*100):.2f}%')
print(f'{((truck_load/all_loads)*100):.2f}%')
print(f'{((train_load/all_loads)*100):.2f}%')



