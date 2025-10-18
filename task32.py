import math

side_a = float(input("Введіть довжину першої сторони трикутника як додатне число (a): "))
side_b = float(input("Введіть довжину другої сторони трикутника як додатне число (b): "))
side_c = float(input("Введіть довжину третьої сторони трикутника як додатне число (c): "))
semi_perimeter = (side_a + side_b + side_c) / 2
area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))
print(f"Площа трикутника з сторонами {side_a}, {side_b}, {side_c} дорівнює {area}.")
