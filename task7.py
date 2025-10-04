operator = input("Введіть назву вашого мобільного оператора (наприклад: Kyivstar, Vodafone, Lifecell): ")
balance_str = input("Введіть ваш поточний баланс у гривнях (наприклад: 125.50): ")

try:
    balance = float(balance_str)
except ValueError:
    balance = 0.0
    print("Ви ввели некоректне число, баланс встановлено в 0.0 грн")

print(f"Вітаємо, абонент мережі {operator}! Ваш поточний баланс становить {balance} грн.")
