# Вывести первые N чисел кратные M и больше K
n = int(input('Insert n: '))
m = int(input('Insert m: '))
k = int(input('Insert k: '))
count = 0
i = k
while count < n:
    i += 1
    if not i % m:
        print(i, end='\t')
        count += 1
