number = []
result = 0
for i in range(int(input())):
    number.append(int(input()))
p = int(input())
q = int(input())
for i in range(p - 1, q):
    result += number[i]
print(result)
