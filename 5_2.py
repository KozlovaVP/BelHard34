# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
number1 = int(input('Insert the first number: '))
operation = int(input('''Choose the operation:
 1 - Addition
 2 - Subtraction
 3 - Multiplication 
 4 - Division
 '''))
while operation not in range(1, 5):
    operation = int(input('Choose the correct number of operation: '))
number2 = int(input('Insert the second number: '))
if operation == 1:
    print('The result is: ' + f'{number1 + number2}')
elif operation == 2:
    print('The result is: ' + f'{number1 - number2}')
elif operation == 3:
    print('The result is: ' + f'{number1 * number2}')
else:
    print('The result is: ' + f'{number1 / number2}')