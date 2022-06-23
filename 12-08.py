text = input().lower()
max_amount = 0
char = ''
for i in range(len(text)):
    amount = text.count(text[i])
    if amount > max_amount:
        max_amount = amount
        char = text[i]
print(char)
