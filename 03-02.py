password = input()
repass = input()
if password != repass:
    print('Различаются.')
elif len(password) < 8:
    print('Короткий!')
else:
    print('OK')
