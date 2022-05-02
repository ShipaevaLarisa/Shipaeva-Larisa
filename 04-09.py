num = int(input())
count = 1
row = ((num * 2 - 1) // 2) + 1
for i in range(1, num + 1):
    print(" " * row, "*" * count)
    count += 2
    row -= 1
