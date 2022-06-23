number = int(input())
for i in range(number):
    word = input().lower()
    if 'кот' in word:
        print(i + 1, word.find('кот') + 1)
