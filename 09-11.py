amount_1 = int(input())
list_1 = []
list_2 = []
for i in range(amount_1):
    list_11 = input()
    list_1.append(list_11)
amount_2 = int(input())
for j in range(amount_2):
    list_22 = input()
    list_2.append(list_22)
for elem in list_2:
    if elem in list_1:
        print(elem)
