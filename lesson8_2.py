# Дан файл с текстом, необходимо сказать сколько слов и букв в каждой строке данного файла
# Результат записать в файл output.txt в формате: в 1 строке N слов M букв

with open('src/input2.txt', 'r', encoding='utf-8') as file:
    i = 1
    result = []
    for line in file:
        space_count = line.count(' ')
        if space_count:
            space_count += 1
        letter_count = 0
        for letter in line:
            if letter.isalpha():
                letter_count += 1
        result.append(f'В {i} строке {space_count} слов {letter_count} букв')
        i += 1

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(result))
