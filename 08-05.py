number = int(input())
text_1 = list()
for i in range(number):
    text_2 = input()
    if text_2[:3] == "Не " or text_2[:3] == "не ":
        text_1.append(text_2[3:])
    else:
        text_1.append(text_2)
print('\n'.join(text_1))
