#Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
#словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
#имена тех, у кого не указана почта (нет ключа email или значение этого ключа - пустая строка)
data = {
    1: {
        'name': 'name1',
        'surname': 'surname1',
        'phone': '1111',
        'email': 'email1',
    },
    2: {
        'name': 'name2',
        'surname': 'surname2',
        'phone': '2222',
        'email': '',
    },
    3: {
        'name': 'name3',
        'surname': 'surname3',
        'phone': '3333'
    },
    4: {
        'name': 'name4',
        'surname': 'surname4',
        'phone': '4',
        'email': 'email4',
    }
}
value = list(data.values())
for i in range(len(value)):
    if value[i].get('email') == '' or value[i].get('email') is None:
        print(value[i].get('name'))
