n = int(input())
x = 0
for i in range(0, n):
    y = int(input())
    if i % 2 == 0:
        x += y
    else:
        x -= y
print(x)
