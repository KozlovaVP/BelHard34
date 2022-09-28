# **Вывести четные числа от 2 до N по 5 в строку
n = int(input('Insert n: '))
count = 0
for i in range(2, n + 1, 2):
    print(i, end = '\t')
    count += 1
    if not i % 5:
        print(end = '\n')


