kol_chisel = 0
n = int(input())
for i in range(1,n+1):
    if n % i == 0:
        kol_chisel = kol_chisel+1
        print(i, end=' ')
print()
if kol_chisel > 2:
    print('НЕТ')
else:
    print('ПРОСТОЕ')
