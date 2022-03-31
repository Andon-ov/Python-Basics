# 6.	Сумиране на гласните букви
# Да се напише програма, която чете текст (стринг), въведен от потребителя,
# и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:

# буква	    a	e	i	o	u
# стойност	1	2	3	4	5


# вход	   изход	коментар
# hello	    6	    e + o = 2 + 4 = 6
# hi	    3	    i = 3
# bamboo	9	    a + o + o = 1 + 4 + 4 = 9
# beer	    4	    e + e = 2 + 2 = 4
text = input()
sum = 0
for letter in text:

    if letter == 'a':
        sum += 1
    elif letter == 'e':
        sum += 2
    elif letter == 'i':
        sum += 3
    elif letter == 'o':
        sum += 4
    elif letter == 'u':
        sum += 5

print(sum)