password = False
while not password:
    print('Введите ваш пароль: ')
    input_password = input()
    if len(input_password) < 8:
        print("Короткий!")
    elif "123" in input_password:
        print("Простой!")
    else:
        print("Подтвердите ваш пароль: ")
        repeat_password = input()
        if repeat_password == input_password:
            print("OK")
            password = True
        else:
            print("Различаются.")

