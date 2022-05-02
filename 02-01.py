town_1 = input()
town_2 = input()
tula = 'Тула'
penza = 'Пенза'
if town_1 != town_2 and (town_1 == tula and town_2 != penza or town_2 == penza and town_1 != tula):
    print('ДА')
else:
    print('НЕТ')
