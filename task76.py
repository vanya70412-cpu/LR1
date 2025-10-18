days = int(input("Введіть кількість днів канікул: "))

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("Перетворення кількості днів канікул у години, хвилини та секунди:")
print(f"{hours:<10}hours")
print(f"{minutes:<10}minutes")
print(f"{seconds:<10}seconds")
