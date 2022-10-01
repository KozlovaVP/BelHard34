#Дан словарь, ключ - Название страны, значение - список городов, на вход
#поступает город, необходимо сказать из какой он страны
dct = {
    'Belarus': ['Minsk', 'Brest', 'Gomel'],
    'France': ['Paris', 'Marseille', 'Aix-en-Provence'],
    'Italy': ['Venice', 'Rome', 'Milan']
}
city = input('Insert a city: ')
value = list(dct.values())
key = list(dct.keys())
for i in range(len(value)):
    for j in range(len(value[i])):
        if city == value[i][j]:
            country = key[i]
            break
print(country)
