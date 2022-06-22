amount = int(input())
name = []
for i in range(amount):
    name_1 = input()
    name.append(name_1)
k = int(input())
for i in range(0 + k - 1, len(name) - 1, k - 1):
    name.remove(name[i])
for elem in name:
    print(elem)
