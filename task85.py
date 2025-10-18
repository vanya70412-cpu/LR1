print('*** Перевірка симетрії числа (до 4 знаків) ***')

number_input = int(input('Введіть ціле число (від 0 до 9999) для перевірки симетрії: '))

four_digit_str = f"{number_input:04d}"


digit_1 = four_digit_str[0]
digit_2 = four_digit_str[1]
digit_3 = four_digit_str[2]
digit_4 = four_digit_str[3]

is_symmetric = (digit_1 == digit_4) and (digit_2 == digit_3)

result = int(is_symmetric)


print(f"Вхідне число: {number_input}")
print(f"Обробка: число доповнено до 4 знаків: {four_digit_str}")
print(f"Порівнюємо: Перша ({digit_1}) <-> Остання ({digit_4}) та Друга ({digit_2}) <-> Передостання ({digit_3})")
print(f"Результат: {result} (1 - симетричне, 0 - не симетричне)")
