n = int(input())
town = set()
for elem in range(n):
    new_town = input()
    town.add(new_town)
last_town = input()
if last_town in town:
    print('TRY ANOTHER')
else:
    print('OK')
