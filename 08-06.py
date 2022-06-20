length = int(input())
amount = int(input())
text = []
for i in range(amount):
    text_1 = input()
    if len(text_1) > length:
        text.append(text_1[:length - 3] + '...')
    else:
        text.append(text_1)
print('\n'.join(text))
