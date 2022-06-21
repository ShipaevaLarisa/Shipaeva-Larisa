text = list()
search_list = list()
result_list = list()
for i in range(int(input())):
    text.append(input())
for i in range(int(input())):
    search_list.append(input())
for i in range(len(search_list)):
    for j in range(len(text)):
        if search_list[i] in text[j]:
            if text[j] in result_list:
                print(text[j])
            else:
                result_list.append(text[j])
