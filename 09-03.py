amount = int(input())
text = []
for i in range(amount):
    text_1 = input()
    text.append(text_1)
number = int(input())
for elem in text:
    if number <= len(elem):
        print(elem[number - 1], end='')
