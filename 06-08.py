N = int(input())
count = 0
names = set()
names_1 = set()
for i in range(N):
    name = input()
    if name in names:
        count += 1
        names_1.add(name)
    names.add(name)
print(count + len(names_1))
