text = input('Input a string: ')
data = {i: text.count(i) for i in text}
print(data)