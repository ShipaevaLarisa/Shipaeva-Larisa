amount = int(input())
number = []
result = False
for i in range(amount):
    number_1 = int(input())
    number.append(number_1)
number_2 = int(input())
for i in range(len(number)):
     for j in range(len(number) - i):
        if (number[i] * number[j]) == number_2:
            result = True
if result:
    print("ДА")
else:
    print("НЕТ")
