
def calculate_sum_and_average(array):
    total_sum = sum(array)
    average = total_sum / len(array) if array else 0
    return total_sum, average

# Пример массивов
array1 = [1, 2, 3, 4, 5]
array2 = [10, 20, 30]
array3 = [-1, -2, -3, -4, -5, -6]

# Вычисляем сумму и среднее арифметическое для каждого массива
result1 = calculate_sum_and_average(array1)
result2 = calculate_sum_and_average(array2)
result3 = calculate_sum_and_average(array3)

# Выводим результаты
print(f"Массив 1: Сумма = {result1[0]}, Среднее арифметическое = {result1[1]}")
print(f"Массив 2: Сумма = {result2[0]}, Среднее арифметическое = {result2[1]}")
print(f"Массив 3: Сумма = {result3[0]}, Среднее арифметическое = {result3[1]}")

