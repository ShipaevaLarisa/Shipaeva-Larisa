set1 = set()
set2 = set()
set3 = set()
m = int(input())
n = int(input())
k = int(input())
for i in range(m + n + k):
    word = input()
    if word in set2:
        set2.discard(word)
    if word in set1:
        set2.add(word)
        set1.discard(word)
    else:
        set1.add(word)
print(len(set2))
