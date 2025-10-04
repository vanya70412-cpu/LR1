total_seconds = int(input("Введіть кількість секунд, яку потрібно перетворити (наприклад: 123456): "))

days = total_seconds // 86400
hours = (total_seconds % 86400) // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("Результат перетворення секунд у формат дні/години/хвилини/секунди:")
print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s).")
