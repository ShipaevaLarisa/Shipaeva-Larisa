word = []
number = int(input())
for i in range(number):
    word_1 = input()
    word.append(word_1)
for i in range(len(word)):
    for j in range(i + 1, len(word)):
        if word[i] > word[j]:
            word[i], word[j] = word[j], word[i]
for elem in word:
    print(elem)
