
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!"  и програмата да приключи.
balance = 0


while True:
    income_money = input()
    if income_money == "NoMoreMoney":
        break

    elif float(income_money) < 0:
        print("Invalid operation!")
        break
    balance += float(income_money)
    print(f"Increase: {float(income_money):.2f}")

print(f"Total: {balance:.2f}")


