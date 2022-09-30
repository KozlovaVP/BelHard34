#Дан список чисел, необходимо его развернуть без использования метода revese и
#функции reversed, а так же дополнительного списка и среза
lst = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(int(len(lst) / 2)):
    num = lst[i]
    lst[i] = lst[len(lst) -1 - i]
    lst[len(lst) - 1 - i] = num
print(lst)