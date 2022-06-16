M = int(input())
N = int(input())
set1 = set()
set2 = set()
for elem in range(M):
    name = input()
    set1.add(name)
for elem in range(N):
    name = input()
    set2.add(name)
    if name in set1:
        print('YES')
    else:
        print('NO')

