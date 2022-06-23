message_1 = ''


def print_without_duplicates(message):
    global message_1
    if message_1 != message:
        print(message)
    message_1 = message
