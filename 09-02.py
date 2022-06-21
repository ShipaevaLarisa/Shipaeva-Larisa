number = int(input())
text = []
for i in range(number):
    text_1 = input()
    text.append(text_1)
search_string = input()
for elem in text:
    if search_string in elem:
        print(elem)
