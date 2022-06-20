name = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890_'
for i in range(len(name)):
    if name[i] not in alphabet:
        print('Неверный символ:', name[i])
        break
else:
    print('OK')
