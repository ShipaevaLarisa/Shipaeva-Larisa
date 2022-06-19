word_1 = input()
while True:
    word_2 = input()
    if word_1[-1] == word_2[0]:
        word_1 = word_2
    else:
        print(word_2)


