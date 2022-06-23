number_1 = input().split()
number_2 = input().split()
print(sum([int(number_1[i]) for i in range(int(number_2[0]), int(number_2[1]) + 1)]))
