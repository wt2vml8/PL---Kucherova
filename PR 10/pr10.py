def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = []
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

def find_rows_with_extreme_sums(matrix):
    max_sum = float('-inf')
    min_sum = float('inf')
    max_row = []
    min_row = []

    for row in matrix:
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum = row_sum
            max_row = row
        if row_sum < min_sum:
            min_sum = row_sum
            min_row = row

    return max_row, min_row, max_sum, min_sum

def write_results_to_file(filename, max_row, max_sum, min_row, min_sum):
    with open(filename, 'w') as file:
        file.write(f"Строка с наибольшей суммой элементов: {' '.join(map(str, max_row))}\n")
        file.write(f"Сумма элементов: {max_sum}\n")
        file.write(f"Строка с наименьшей суммой элементов: {' '.join(map(str, min_row))}\n")
        file.write(f"Сумма элементов: {min_sum}\n")

if __name__ == "__main__":
    # Чтение матрицы из файла
    input_filename = 'C:\\Users\\Honor\\Desktop\\языки программирования\\PR 10\\Kucherova_UB-42_vvod.txt'
    matrix = read_matrix_from_file(input_filename)

    # Нахождение строк с наибольшей и наименьшей суммой элементов
    max_row, min_row, max_sum, min_sum = find_rows_with_extreme_sums(matrix)

    # Запись результата в файл
    output_filename = 'C:\\Users\\Honor\\Desktop\\языки программирования\\PR 10\Kucherova_UB-42_vivod.txt'
    write_results_to_file(output_filename, max_row, max_sum, min_row, min_sum)



