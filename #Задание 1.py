#Задание 1

def calculate_area_perimeter(length, width):
area = length * width
perimeter = 2 * (length + width)
return area, perimeter

# Получаем вводимые значения
try:
length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))

# Проверяем, что введенные числа положительные
if length > 0 and width > 0:
area, perimeter = calculate_area_perimeter(length, width)
print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")
else:
print("Длина и ширина должны быть положительными числами.")
except ValueError:
print("Введено некорректное значение. Пожалуйста, введите числовые значения.")