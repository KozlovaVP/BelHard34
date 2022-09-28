text1 = input('Insert a text: ')
text2 = input('Insert a key: ')
while len(text1) != len(text2):
    print('The text and the key have to be the same length!')
    text1 = input('Insert the text again: ')
    text2 = input('Insert the key again: ')

for i in range(len(text1)):
    char = bin(ord(text1[i]))[2:]
    char = "0" * (8 - len(char)) + char
    print(char, end='\t')
print(end='\n')

for i in range(len(text2)):
    char = bin(ord(text2[i]))[2:]
    char = "0" * (8 - len(char)) + char
    print(char, end='\t')
print(end='\n')

result = ''
for i in range(len(text2)):
    char1 = bin(ord(text1[i]))[2:]
    char1 = "0" * (8 - len(char1)) + char1
    char2 = bin(ord(text2[i]))[2:]
    char2 = "0" * (8 - len(char2)) + char2
    for k in range(len(char1) + 1):
        if not k % 8 and k != 0:
            result += '\t'
        elif char1[k] == char2[k]:
            result += '0'
        else:
            result += '1'
print('Result:')
print(result)

