amount = int(input())
numbers = []
for i in range(amount):
    number = input()
    numbers.append(number)
for j in range(amount):
    print(int(numbers[j]) + int(numbers[j + 1]))
