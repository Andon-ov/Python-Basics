# Задача 1. Приход от филм

# Прожекцията на филма трае предварително зададен брой дни, като всеки ден се продават определен брой билети.
# Цената на 1 билет се определя от студиото. За излъчване на продукцията, определен процент от общия приход остава за киното.

movie_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
percentage_for_cinema = int(input())
total = ((number_of_days * number_of_tickets) * ticket_price) * (percentage_for_cinema  - 100) / 100
print(f"The profit from the movie {movie_name} is {abs(total):.2f} lv.")


