n = int(input())
for i in range(n):
    text = input()
    if ('кот' in text) or ('Кот' in text):
        print('МЯУ')
        break
else:
    print('НЕТ')
