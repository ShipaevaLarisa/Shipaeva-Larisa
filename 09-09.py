amount = []
for i in range(int(input())):
    amount.append(int(input()))
for elem in amount:
    print(elem)
print()
for i in range(len(amount)):
    print(amount[i] * 3)
