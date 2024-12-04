import re

# Import data
with open('example.txt', 'r') as file:
    example_data = [list(line.strip()) for line in file]

def get_sum_part_number(data):
    sym_indexes = []
    symbols = {'#', '$', '%', '&', '*', '+', '-', '/', '=', '@'}
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] in symbols:
                sym_indexes.append(str(row) + str(col))
    for row in range(len(data)):
        for col in range(len(data[row])):
            num = ''
            current = data[row][col]
            next = data[row][col+1]
            if current.isdigit():
                if next.isdigit():
                    num += num
            else:
                num = ''

        print(num)


    print(sym_indexes)
    return 4361

value = get_sum_part_number(example_data)
print(value)