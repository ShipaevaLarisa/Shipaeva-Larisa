number = input().split(' ')
print(' '.join([str(int(number[i]) ** 2) for i in range(len(number)) if str(int(number[i]) ** 2)[-1] != '9' and i % 2 == 0]))
