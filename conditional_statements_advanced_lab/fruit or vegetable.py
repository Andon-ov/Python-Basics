# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт.
product = input()
if product in 'banana''apple''kiwi''cherry''lemon''grapes':
    print('fruit')
elif product in 'tomato''cucumber''pepper''carrot':
    print('vegetable')
else:
    print('unknown')