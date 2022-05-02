print('Введите логин')
login = input()
print('Введите резервный адрес электронной почты')
email = input()
if '@' in login:
    print('Некорректный логин')
elif not '@' in email:
    print('Некорректный адрес')
else:
    print('ОК')

