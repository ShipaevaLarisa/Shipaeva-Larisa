text = []
for i in range(int(input()[1:])):
    text_1 = input()
    if '#' in text_1.split():
        f = text_1.index('#')
        text_1 = ''.join(text_1[:f])
    text.append(text_1)
for i in range(len(text)):
    print(text[i])
