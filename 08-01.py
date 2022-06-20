words = set()
max_word = ''
min_word = ''
while True:
    word = input()
    if word == 'стоп':
        break
    words.add(word)
for word in words:
    if len(word) > len(max_word):
        max_word = word
    elif len(word) < len(min_word) or len(min_word) == 0:
        min_word = word
if len(set(min_word) - set(max_word)) == 0:
    print('ДА')
else:
    print('НЕТ')
