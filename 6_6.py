#Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst1 = list(filter(lambda x: not x % 2, lst))
lst2 = list(filter(lambda x: x % 2, lst))
print(lst1 + lst2)