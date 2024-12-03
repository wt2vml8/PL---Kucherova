def read_file(filename):
    with open(filename, 'r') as file:
        matrix = []
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

def find_sums(matrix):
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

def write_resul(filename, max_row, max_sum, min_row, min_sum):
    with open(filename, 'w') as file:
        file.write(f'Строка с наибольшей суммой: {' '.join(map(str, max_row))}\n')
        file.write(f'Наибольшая сумма: {max_sum}\n')
        file.write(f'Строка с наименьшей суммой: {' '.join(map(str, min_row))}\n')
        file.write(f'Наименьшая сумма: {min_sum}\n')

if __name__ == "__main__":
   
    input_filename = 'C:\\Users\\Honor\\Desktop\\языки программирования\\PR 10\\Kucherova_UB-42_vvod.txt'
    matrix = read_file(input_filename)

    max_row, min_row, max_sum, min_sum = find_sums(matrix)

    output_filename = 'C:\\Users\\Honor\\Desktop\\языки программирования\\PR 10\Kucherova_UB-42_vivod.txt'
    write_resul(output_filename, max_row, max_sum, min_row, min_sum)



