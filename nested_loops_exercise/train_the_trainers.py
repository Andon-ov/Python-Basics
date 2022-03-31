# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито,
# което ще оценява презентациите, като напишете програма, в която да изчислява средната оценка от представянето
# на всяка една презентация от даден студент, а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.


average_score = 0
score_counter = 0
all_scores = 0

people_in_jury = int(input())
presentation_name = input()

while presentation_name != "Finish":
    total_score = 0
    for people in range(1, people_in_jury + 1):
        current_score = float(input())
        score_counter += 1
        total_score += current_score
    average_score = total_score / people_in_jury
    all_scores += total_score
    print(f"{presentation_name} - {average_score:.2f}.")
    presentation_name = input()
print(f"Student's final assessment is {all_scores / score_counter:.2f}.")