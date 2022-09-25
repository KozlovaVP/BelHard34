string = input('Input a string: ')
# the first solution:
print(string.replace(' ', '-'))
# the second solution:
string = string.split(' ')
string = '-'.join(string)
print(string)
