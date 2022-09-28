n = int(input('Insert a number: '))
users = {
    i: {
        'name': input(f'{i} name: '),
        'email': input(f'{i} email: ')
    } for i in range(n)
}
print(users)