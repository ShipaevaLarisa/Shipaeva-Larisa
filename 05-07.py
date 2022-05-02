peace = 'Остазия'
war = 'Евразия'
for i in range(int(input())):
    q = input()
    if q == 'С кем война?':
        print(war)
    if q == 'С кем мир?':
        print(peace)
    if q == 'Меняем':
        peace, war = war, peace
