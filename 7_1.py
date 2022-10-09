text = '''
iPhone 14 Pro Max

ru from 1 1800

ru from 5 1700

en from 1 1600

iPhone 14 Pro

ru from 50 1500

en from 5 1400

en from 20 1300
'''
countries = ['ru', 'en', 'fr', 'ch']
from_to = ['from 1', 'from 5', 'from 20', 'from 50']

# data = {
#    'iPhone 14 Pro Max': {
#        'ru': {
#            'from 1': 1800,
#            'from 5': 1700
#        },
#        'en': {
#            'from 1': 1600
#        }
#    },
#    'iPhone 14 Pro': {
#        'ru': {
#            'from 50': 1500
#        },
#        'en': {
#            'from 5': 1400,
#            'from 20': 1300
#        }
#    }
# }
text = text.replace('from ', 'from_')  # replace to split then by ' '
text = list(filter(lambda x: x, text.split('\n')))  # create a list of strings without emply rows
# if string doesn't start from anything in countries, hence it's a name of device
data = {}
flag = ''  # for a name of device (to know to which device other rows belong)
for line in text:
    if line[:2] not in countries:
        data[line] = {}  # created {'iPhone 14 Pro Max': {}, 'iPhone 14 Pro': {}}
        flag = line  # to remember the last found device
    else:
        line = line.split()  # each line will be split into 3 elements (list): ['ru', 'from 1', '1500']
        if line[0] not in data[flag]:  # if the country is not added yet
            data[flag][line[0]] = {line[1]: int(line[2])}  # add the new country
        else:
            data[flag][line[0]].update({line[1]: int(line[2])})  # update already existing country
print(data)
