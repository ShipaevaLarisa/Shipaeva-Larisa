number = int(input())
text = []
for i in range(number):
    text_1 = input()
    if text_1[:2] == "%%":
        text.append(text_1[2:])
    elif text_1[:4] == "####":
        continue
    else:
        text.append(text_1)
for elem in text:
    print(elem)
