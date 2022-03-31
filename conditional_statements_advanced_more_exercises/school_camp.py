# 7.	Ученически лагер
# Частно училище организира лагери за учениците по време на ваканциите.
# В зависимост от вида на ваканцията (пролетна, лятна или зимна) и вида на групата (момчета/момичета или смесена)
# цената на нощувката в хотела е различна, както и спортът, който ще практикуват учениците.
#
# 	    			                    Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момчета/момичета		    9.60		                    	7.20				                15
# смесена група			         10				                9.50				                20

# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка

# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата:
# 			        	Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момичета		Gymnastics		Athletics			    Volleyball
# момчета			    Judo			Tennis				    Football
# смесена група	Ski				Cycling				Swimming
# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта,
# който ще се практикува от учениците.
# Вход
# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището,
# форматирана до втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“
season = input()
type_of_group = input()
number_of_student = int(input())
number_of_nights = int(input())
sport = ''
price = 0
if season == 'Winter':
    if  type_of_group == 'girls':
        sport = 'Gymnastics'
        price = number_of_student * (9.60 * number_of_nights)
    elif  type_of_group == 'boys':
        sport = 'Judo'
        price = number_of_student * (9.60 * number_of_nights)
    elif  type_of_group == 'mixed':
        sport = 'Ski'
        price = number_of_student * (10 * number_of_nights)
elif season == 'Spring':
    if  type_of_group == 'girls':
        sport = 'Athletics'
        price = number_of_student * (7.20 * number_of_nights)
    elif  type_of_group == 'boys':
        sport = 'Tennis'
        price = number_of_student * (7.20 * number_of_nights)
    elif  type_of_group == 'mixed':
        sport = 'Cycling'
        price = number_of_student * (9.50 * number_of_nights)
elif season == 'Summer':
    if  type_of_group == 'girls':
        sport = 'Volleyball'
        price = number_of_student * (15 * number_of_nights)
    elif  type_of_group == 'boys':
        sport = 'Football'
        price = number_of_student * (15 * number_of_nights)
    elif  type_of_group == 'mixed':
        sport = 'Swimming'
        price = number_of_student * (20 * number_of_nights)
# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
if 10 <= number_of_student < 20:
    price *= 0.95
elif 20 <= number_of_student < 50:
    price *= 0.85
elif number_of_student >= 50:
    price *= 0.50


print(f'{sport} {price:.2f} lv.')