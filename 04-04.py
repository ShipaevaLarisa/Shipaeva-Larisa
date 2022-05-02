n = int(input())
if n > 0:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)
elif n == 0:
    print('1')

