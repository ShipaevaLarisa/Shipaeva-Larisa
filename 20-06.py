list_1 = []

while True:
    word = input()
    if word == '':
        break
    list_1.append(word)

print(*sorted(list_1, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')
