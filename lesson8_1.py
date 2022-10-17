# Дан файл с числами через запятую (могут быть пробелы)
# прочитать файл в список списков чисел (int)

with open('src/input.txt', 'r', encoding='utf-8') as file:
    lines = []
    for line in file:
        line = line.strip().replace(' ', '')
        numbers = list(map(int, line.split(',')))
        lines.append(numbers)
    print(lines)

# Через генератор:
# with open('src/input.txt', 'r', encoding='utf-8') as file:
#   lines = [list(map(int, line.strip().replace(' ', '').split(','))) for line in file]
# print(lines)
