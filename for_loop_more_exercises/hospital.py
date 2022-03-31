# # 2.	Болница
# # За даден период от време, всеки ден в болницата пристигат пациенти за преглед. Тя разполага първоначално със 7 лекари.
# # Всеки лекар може да преглежда само по един пациент на ден, но понякога има недостиг на лекари,
# # затова останалите пациенти се изпращат в други болници
#
# # Всеки трети ден,болницата прави изчисления и ако броят на непрегледаните пациенти е по-голям от броя на прегледаните,
# # се назначава още един лекар. Като назначаването става преди да започне приемът на пациенти за деня.
#
# # Напишете програма, която изчислява за дадения период броя на прегледаните и непрегледаните пациенти.
# # Вход
#
n = int(input())
doctors = 7
number_patients_examined = 0
total_number_patients_examined = 0
number_patients_unexamined = 0
total_number_patients_unexamined = 0

for i in range(1, n + 1):

    number_of_patients = int(input())
    if i % 3 == 0:
        if total_number_patients_unexamined > total_number_patients_examined:
            doctors += 1
    if number_of_patients <= doctors:
        number_patients_examined = number_of_patients
        number_patients_unexamined = 0

    else:
        number_patients_examined = doctors
        number_patients_unexamined = number_of_patients - number_patients_examined

    total_number_patients_unexamined += number_patients_unexamined
    total_number_patients_examined += number_patients_examined

print(f'Treated patients: {total_number_patients_examined}.')
print(f'Untreated patients: {total_number_patients_unexamined}.')


