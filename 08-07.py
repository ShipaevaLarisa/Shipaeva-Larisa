number = int(input())
for i in range(number):
    text = input()
    if 'кот' in text.lower():
        print(i + 1, text.lower().find("кот") + 1)
