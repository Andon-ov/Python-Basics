annual_tax = int(input())
# Баскетболни кецове – цената им е 40% по-малка от таксата за една година
sneakers_price = annual_tax * 0.6
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
dress_price = sneakers_price * 0.8
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
ball_price = dress_price / 4
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
acc_price = ball_price / 5
total_sum = annual_tax + sneakers_price + dress_price + ball_price + acc_price
print(f'{total_sum:.2f}')