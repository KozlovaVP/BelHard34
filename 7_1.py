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

data = {
    'iPhone 14 Pro Max': {
        'ru': {
            'from 1': 1800,
            'from 5': 1700
        },
        'en': {
            'from 1': 1600
        }
    },
    'iPhone 14 Pro': {
        'ru': {
            'from 50': 1500
        },
        'en': {
            'from 5': 1400,
            'from 20': 1300
        }
    }
}
result = []
j = 0
i = 0
for i in range(len(text)):
    if text[i] != '\n':
        j = i
        while text[i] != '\n' and j < len(text):
            #result[j] = ''
            result[j][i].append(text[i])
            i += 1
        j += 1
    else:
        i += 1
print(result)