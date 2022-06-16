M = int(input())
N = int(input())
English = set()
German = set()
for elem in range(M):
    last_name1 = input()
    English.add(last_name1)
for elem in range(N):
    last_name2 = input()
    German.add(last_name2)
result = English.symmetric_difference(German)
if len(result) == 0:
    print('NO')
else:
    print(len(result))
