def ask_password():
    password = input('Введите пароль: ')
    if password == '1234':
        print('Пароли совпадают')
    else:
        print('Пароли не совпадают')


ask_password()