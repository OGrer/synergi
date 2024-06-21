def compute_value(number):
# Преобразуем число в строку, чтобы легко получить каждую цифру
str_number = str(number)

# Извлекаем цифры
tens_of_thousands = int(str_number[0]) # десятки тысяч
thousands = int(str_number[1]) # тысячи
hundreds = int(str_number[2]) # сотни
tens = int(str_number[3]) # десятки
units = int(str_number[4]) # единицы

# Возводим десятки в степень единиц
step1 = tens * units

# Умножаем на количество сотен
step2 = step1 * hundreds

# Вычисляем разность между десятками тысяч и тысячами
difference = tens_of_thousands - thousands

# Делим результат на разность
result = step2 / difference

return float(result)

# Пример использования
example_number = 46275
result = compute_value(example_number)
print(result) # Ожидается -16807.0