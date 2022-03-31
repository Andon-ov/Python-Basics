# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
deposit = float(input())
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
months = int(input())
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]
annual_interest_precent = float(input())
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# смятаме годишния лихвен процент
annual_interest = deposit * annual_interest_precent / 100
# смятаме стойноста за месец
monthly_interest = annual_interest / 12
# цялата сума
total_sum = deposit + (months * monthly_interest)
print(total_sum)