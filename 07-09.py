word = input()
number = int(input())
if number > len(word):
    print('ОШИБКА')
else:
    print(word[number - 1])
