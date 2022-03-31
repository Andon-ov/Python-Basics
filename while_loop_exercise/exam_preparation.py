# 2.	Подготовка за изпит
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки.

# Незадоволителна е всяка оценка, която е по-малка или равна на 4.

# Вход
# •	На първи ред - брой незадоволителни оценки - цяло число;
# •	След това многократно се четат по два реда:
# o	Име на задача – текст;
# o	Оценка - цяло число в интервала [2…6]
number_unsatisfactory_assessments = int(input())
bad_assessments = 0
count = 0
last_problem = ''
evaluation_sum = 0
torn = False
problem_name = input()

while problem_name != "Enough":

    evaluation = int(input())

    if evaluation <= 4:
        bad_assessments += 1
        if bad_assessments == number_unsatisfactory_assessments:
            torn = True
            break

    last_problem = problem_name
    evaluation_sum += evaluation
    count += 1

    problem_name = input()


if torn:
    print(f"You need a break, {number_unsatisfactory_assessments} poor grades.")

else:
    print(f"Average score: {(evaluation_sum/ count):.2f}")
    print(f"Number of problems: {count}")
    print(f"Last problem: {last_problem}")



# •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:

# o	"Average score: {средна оценка}"
# o	"Number of problems: {броя на всички задачи}"
# o	"Last problem: {името на последната задача}"

# •	Ако получи определеният брой незадоволителни оценки:

# o	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.
