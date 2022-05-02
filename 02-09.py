height_1 = int(input())
height_2 = int(input())
height_3 = int(input())
if height_1 < height_2:
    height_1, height_2 = height_2, height_1
if height_2 < height_3:
    height_2, height_3 = height_3, height_2
if height_1 < height_2:
    height_1, height_2 = height_2, height_1
print(height_1)
print(height_2)
print(height_3)
