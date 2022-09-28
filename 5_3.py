# **Вывести четные числа от 2 до N по 5 в строку
n = int(input('Insert n: '))
for i in range(2, n + 1, 2):
    print(i, end='\t')
    if not i % 5:
        print(end='\n')
