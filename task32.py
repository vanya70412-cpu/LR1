import math

a = float(input("Введіть довжину сторони a трикутника: "))
b = float(input("Введіть довжину сторони b трикутника: "))
c = float(input("Введіть довжину сторони c трикутника: "))

s = (a + b + c) / 2
under_sqrt = s * (s - a) * (s - b) * (s - c)

if under_sqrt <= 0:
    print("Задані сторони не утворюють правильний трикутник.")
else:
    area = math.sqrt(under_sqrt)
    print(f"Площа трикутника за формулою Герона дорівнює: {area}")
