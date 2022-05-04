page_1 = set()
page_2 = set()
num_1 = input()
while num_1 != '':
    page_1.add(num_1)
    num_1 = input()
page_1.add(num_1)
num_2 = input()
while num_2 != '':
    page_2.add(num_2)
    num_2 = input()
intersection = page_1.intersection(page_2)
if not intersection:
    print('EMPTY')
else:
    for i in intersection:
        print(i)

