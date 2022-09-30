# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной стороны списка
lst = [1, 2, 3, 4, 5, 6, 7, 8]
result = []
for i in range(len(lst)):
    if i == 0:
        result.append(lst[i + 1] + lst[len(lst) - 1])
    elif i == len(lst) - 1:
        result.append(lst[i - 1] + lst[-len(lst)])
    else:
        result.append(lst[i - 1] + lst[i + 1])
print(result)
