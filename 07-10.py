number = int(input())
text = input()
for i in text:
    if not i.isalpha():
        print(i, end='')
        continue
    if ord(i) + number > 1071 and ord(i) <= 1071 or ord(i) + number > 1103 and ord(i) <= 1103:
        i = chr(ord(i) - 32)
    i = chr(ord(i) + number)
    print(i, end='')
