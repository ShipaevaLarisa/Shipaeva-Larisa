number = int(input())
result = ''
cat = False
for i in range(number):
    word = input()
    if ("Кот" in word or "кот" in word) and not cat:
        result = "МЯУ"
        cat = True
    elif ("Пёс" in word or "пёс" in word) and cat:
        cat = False
    elif not cat:
        result = "НЕТ"
print(result)
