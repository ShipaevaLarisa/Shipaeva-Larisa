line = 0
i = 0
while True:
    text = input()
    if text == 'СТОП':
        break
    if ('Кот' in text or 'кот' in text) and not line:
        line = i + 1
    i += 1
if not line:
    line = -1
print(line)
