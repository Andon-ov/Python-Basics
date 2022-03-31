# 8.	Навреме за изпит
# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).

# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.

# Ако е пристигнал по-рано повече от 30 минути, той е подранил.
#
# Ако е дошъл след часа на изпита, той е закъснял.

# Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.

# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.

# На първия ред отпечатайте:
# •	"Late", ако студентът пристига по-късно от часа на изпита;
# •	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# •	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# •	"mm minutes before the start" за идване по-рано с по-малко от час;
# •	"hh:mm hours before the start" за подраняване с 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:05”;
# •	 "mm minutes after the start" за закъснение под час;
# •	"hh:mm hours after the start" за закъснение от 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:03”.
hour_of_exam = int(input())
min_of_exam = int(input())
hour_of_arrival = int(input())
min_of_arrival = int(input())
time_of_exam = hour_of_exam * 60 + min_of_exam
time_of_arrival = hour_of_arrival * 60 + min_of_arrival

if time_of_arrival > time_of_exam:
    print('Late')
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print('On time')
else:
    print('Early')
differance = abs(time_of_exam - time_of_arrival)
hour = differance // 60
minutes = differance % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f'{differance} minutes before the start')
elif time_of_arrival <= time_of_exam - 60:
    print(f'{hour}:{minutes:02d} hours before the start')
elif time_of_exam < time_of_arrival <time_of_exam + 60:
    print(f'{differance} minutes after the start')
elif time_of_arrival >= time_of_exam + 60:
    print(f'{hour}:{minutes:02d} hours after the start')