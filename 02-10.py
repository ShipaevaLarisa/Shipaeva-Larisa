x = float(input())
y = float(input())
z = str(input())
if z == '+':
    print(x+y)
elif z == '-':
    print(x-y)
elif z == '*':
    print(x*y)
elif z == '/':
    if y != 0:
        print(x/y)
    elif y == 0:
        print('888888')
else:
    print('888888')
