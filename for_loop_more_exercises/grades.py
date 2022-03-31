
# В началото програмата получава броят на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да изпечата процента на студенти с
# оценка между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече.





number_students_in_exam = int(input())
top_students = 0
average_student = 0
low_student = 0
fail_student = 0
sum = 0
for i in range(number_students_in_exam):
    grade_from_exam = float(input())
    if grade_from_exam < 3:
        fail_student += 1
        sum += grade_from_exam
    elif grade_from_exam < 4:
        low_student += 1
        sum += grade_from_exam
    elif grade_from_exam < 5:
        average_student += 1
        sum += grade_from_exam
    elif grade_from_exam >= 5:
        top_students += 1
        sum += grade_from_exam

average_success = sum / number_students_in_exam
top_students_percentage = (top_students / number_students_in_exam) * 100
average_student_percentage = (average_student / number_students_in_exam) * 100
low_student_percentage = (low_student / number_students_in_exam) * 100
fail_student_percentage = (fail_student / number_students_in_exam) * 100
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -	"Fail: {по-малко от 3.00}%"
# Ред 5 -	"Average: {среден успех}"
# Всички числа трябва да са форматирани до вторият знак след десетичната запетая.

print(f'Top students: {top_students_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {average_student_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {low_student_percentage:.2f}%')
print(f'Fail: {fail_student_percentage:.2f}%')
print(f'Average: {average_success:.2f}')