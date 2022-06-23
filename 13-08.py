dictionary = dict()
for i in range(int(input())):
    text = input().split()
    key = text[0]
    text.remove(key)
    value = ' '.join(text)
    dictionary[key] = value
for i in range(int(input())):
    line = input()
    if line in dictionary:
        print(dictionary.get(line))
    else:
        print('Нет в словаре')
