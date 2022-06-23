text = input().lower()
result = []
for char in set(text):
    result.append(text.count(char))
print(max(result))
