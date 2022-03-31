# Магазин за цветя предлага 3 вида цветя: хризантеми, рози и лалета. Цените зависят от сезона.
# Сезон	          Хризантеми	   Рози	        Лалета
# Пролет / Лято	2.00 лв./бр.	4.10 лв./бр.	2.50 лв./бр.
# Есен / Зима	3.75 лв./бр.	4.50 лв./бр.	4.15 лв./бр.
# В празнични дни цените на всички цветя се увеличават с 15%. Предлагат се следните отстъпки:
# •	За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
# •	За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
# •	За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
# Отстъпките се правят по така написания ред и могат да се наслагват! Всички отстъпки важат след оскъпяването за
# празничен ден!
# Цената за аранжиране на букета винаги е 2лв. Напишете програма, която изчислява цената за един букет.
# Вход
# Входът се чете от конзолата и съдържа точно 5 реда:
# •	На първия ред е броят на закупените хризантеми – цяло число в интервала [0 ... 200]
# •	На втория ред е броят на закупените рози – цяло число в интервала [0 ... 200]
# •	На третия ред е броят на закупените лалета – цяло число в интервала [0 ... 200]
# •	На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
# •	На петия ред е посочено дали денят е празник – [Y – да / N - не]
# Изход
# Да се отпечата на конзолата 1 число – цената на цветята, форматирана до вторият знак след десетичната запетая.

purchased_chrysanthemums = int(input())
purchased_roses = int(input())
purchased_tulips = int(input())
season = str.lower(input())
holiday = str.lower(input())

sum = 0
if season == 'spring':
    purchased_chrysanthemums_sum = 2 * purchased_chrysanthemums
    purchased_roses_sum = 4.1 * purchased_roses
    purchased_tulips_sum = 2.5 * purchased_tulips
    sum = purchased_tulips_sum + purchased_roses_sum + purchased_chrysanthemums_sum
elif season == 'summer':
    purchased_chrysanthemums_sum = 2 * purchased_chrysanthemums
    purchased_roses_sum = 4.1 * purchased_roses
    purchased_tulips_sum = 2.5 * purchased_tulips
    sum = purchased_tulips_sum + purchased_roses_sum + purchased_chrysanthemums_sum
elif season == 'autumn':
    purchased_chrysanthemums_sum = 3.75 * purchased_chrysanthemums
    purchased_roses_sum = 4.5 * purchased_roses
    purchased_tulips_sum = 4.15 * purchased_tulips
    sum = purchased_tulips_sum + purchased_roses_sum + purchased_chrysanthemums_sum
elif season == 'winter':
    purchased_chrysanthemums_sum = 3.75 * purchased_chrysanthemums
    purchased_roses_sum = 4.5 * purchased_roses
    purchased_tulips_sum = 4.15 * purchased_tulips
    sum = purchased_tulips_sum + purchased_roses_sum + purchased_chrysanthemums_sum
# В празнични дни цените на всички цветя се увеличават с 15%. Предлагат се следните отстъпки:
if holiday == 'y':
    sum *= 1.15
# •	За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
if season == 'spring':
    if purchased_tulips > 7:
        sum *= 0.95
# •	За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
if season == 'winter':
    if purchased_roses >= 10:
        sum *= 0.90
# •	За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
# имам грешка в бройката - тъй като променливите носят по големи стойности
if purchased_tulips + purchased_roses + purchased_chrysanthemums > 20:
    sum *= 0.80
print(f'{sum + 2:.2f}')


    # Отстъпките се правят по така написания ред и могат да се наслагват! Всички отстъпки важат след оскъпяването за
    # празничен ден!
    # Цената за аранжиране на букета винаги е 2лв. Напишете програма, която изчислява цената за един букет.