# Предстои Вело състезание за благотворителност в което участниците са разпределени в
# младша("juniors") и старша("seniors") група. Парите се набавят от таксата за участие на велосипедистите.
# Според възрастовата група и вида на трасето на което ще се провежда състезанието, таксата е различна.
# Група	  trail	 cross-country	downhill	road
# juniors	5.50	   8	      12.25	      20
# seniors	7	    9.50	      13.75	 21.50
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши),
# таксата  намалява с 25%. Организаторите отделят 5% процента от събраната сума за разходи.
# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.


numbers_juniors = int(input())
numbers_seniors = int(input())
route_type = str(input())
# sum = numbers_seniors + numbers_juniors
total = 0
if route_type == 'trail':
    numbers_seniors *= 7
    numbers_juniors *= 5.5
    total = (numbers_seniors + numbers_juniors) * 0.95
    print(f'{total:.2f}')

elif route_type == 'cross-country':

    if numbers_juniors + numbers_seniors >= 50:
        numbers_seniors *= 9.5
        numbers_juniors *= 8
        total = ((numbers_seniors + numbers_juniors) * 0.95) * 0.75
        print(f'{total:.2f}')

    elif numbers_juniors + numbers_seniors <= 50:
        numbers_seniors *= 9.5
        numbers_juniors *= 8

        total = (numbers_seniors + numbers_juniors) * 0.95
        print(f'{total:.2f}')

elif route_type == 'downhill':
    numbers_seniors *= 13.75
    numbers_juniors *= 12.25
    total = (numbers_seniors + numbers_juniors) * 0.95
    print(f'{total:.2f}')

elif route_type == 'road':
    numbers_seniors *= 21.5
    numbers_juniors *= 20
    total = (numbers_seniors + numbers_juniors) * 0.95
    print(f'{total:.2f}')
