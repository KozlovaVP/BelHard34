# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
number = int(input('Insert a number: '))

def change_to_bin(number):
    result = ''
    while number:
        if number % 2 == 1:
            number = (number - 1) / 2
            result += '1'
        else:
            number /= 2
            result += '0'
    return result[::-1]

def change_to_ten(number):
    result = 0
    for i in range(len(number)):
        if number[len(number) - 1 - i] == '1':
            result += 2 ** i
    return result

print(change_to_bin(number))
print(change_to_ten(change_to_bin(number)))