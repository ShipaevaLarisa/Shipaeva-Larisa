list_1 = list()
list_2 = list()
for i in range(int(input())):
    number = int(input())
    list_2 = list()
    for j in range(number):
        text = input()
        list_2.append(text)
    list_1.append(list_2)
if any('5' in student for text in list_1 for student in text):
    print('ДА')
else:
    print('НЕТ')
