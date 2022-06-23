def take_large_banknotes(banknotes):
    result = list()
    for banknote in banknotes:
        if banknote > 10:
            result.append(banknote)
    return result
