list_1 = list()


def print_only_new(message):
    text = message.split()
    if text[2] not in list_1:
        list_1.append(text[2])
        print(message)
