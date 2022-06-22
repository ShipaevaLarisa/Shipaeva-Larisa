number = int(input())
surname = []
for i in range(number):
    surname_1 = input()
    surname.append(surname_1)
for elem in surname:
    print(elem)
print()
for elem in surname:
    if int(elem[-1]) > 3:
        print(elem)
