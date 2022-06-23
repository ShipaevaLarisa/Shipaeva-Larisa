def print_document(pages):
    result = list()
    for page in pages:
        page_1 = page.split()
        if page_1[0] == 'Секретно':
            result.append('Дальнейшие материалы засекречены')
            return print(*result, sep="\n")
        result.append(page)
    result.append('Напечатано без купюр')
    return print(*result, sep="\n")
