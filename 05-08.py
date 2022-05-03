text = ''
count = 0
line = -1
i = 1
while text != 'СТОП':
    text = input()
    if 'Кот' in text or 'кот' in text:
        count += 1
    if ('Кот' in text or 'кот' in text) and line == -1:
        line = i
    i += 1
print(count, line)
