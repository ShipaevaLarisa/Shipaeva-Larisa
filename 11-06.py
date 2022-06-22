number = int(input())
text = []
for i in range(number):
    text_1 = input()
    text.append(text_1)
print(', '.join([text[i] for i in range(len(text)) if 'лук' not in text[i].lower()]))
