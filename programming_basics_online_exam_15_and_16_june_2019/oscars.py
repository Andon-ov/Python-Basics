actor_name = input()
academy_points = float(input())
number_evaluators = int(input())

for _ in range(number_evaluators):
    evaluator_name = input()
    evaluator_points = float(input())

    current_final_point = len(evaluator_name) * evaluator_points / 2
    academy_points += current_final_point

    if academy_points > 1250.5:
        break

if academy_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")

if academy_points < 1250.5:
    deff = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {deff:.1f} more!")