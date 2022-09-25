name = input('Input a name: ')
age = input('Input an age: ')
city = input('Input a city: ')
# the first solution:
print('Hello ' + name + ' (' + age + ' years old, from ' + city + ')!')
# the second solution:
print('Hello %s (%s years old, from %s)!' % (name, age, city))
# the third solution:
print('Hello {} ({} years old, from {})!'.format(name, age, city))