alphabet = "ABCDEFGHI"
number_1 = int(input())
number_2 = number_1
if 0 < number_1 <= 9:
    for i in range(number_1):
        for j in range(number_1):
            print(alphabet[j] + str(number_2), end="\t")
            j += 1
        print()
        number_2 -= 1


