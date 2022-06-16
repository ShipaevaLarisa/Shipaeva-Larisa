name1 = set()
name2 = set()
number_dishes1 = int(input())
for i in range(number_dishes1):
    name_dishes1 = input()
    name1.add(name_dishes1)
number_days = int(input())
for j in range(number_days):
    number_dishes2 = int(input())
    for k in range(number_dishes2):
        name_dishes2 = input()
        name2.add(name_dishes2)
print(*sorted(name1 - name2), sep='\n')




