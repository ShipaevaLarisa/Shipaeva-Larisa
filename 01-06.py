print('Любите ли вы котиков?')
answer_1 = input()
print('Умеете ли вы программировать?')
answer_2 = input()
if answer_1 == 'да' and answer_2 == 'да':
    print('Вы обладаете незаурядным умом.')
elif answer_1 == 'нет' and answer_2 == 'нет':
    print('Вы странный человек.')
elif answer_1 == 'да' and answer_2 == 'нет':
    print('У вас доброе сердце.')
elif answer_1 == 'нет' and answer_2 == 'да':
    print('Вы умны.')
else:
    print('Ошибка')


