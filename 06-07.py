M = int(input())
lst = [set(input() for _ in range(int(input()))) for _ in range(M)]
res = lst[0]
for i in lst:
    res = res.intersection(i)
print(*sorted(res),sep='\n')
