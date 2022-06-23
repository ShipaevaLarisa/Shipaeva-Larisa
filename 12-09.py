letter = input().lower()
text = input().split()
for elem in text:
    if letter in elem.lower():
        print(elem)
