text = input().split()
result = ''
for elem in text:
    result += '-'.join(list(elem)) + ' '
print(result.upper())
