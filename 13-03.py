alphabet = {
    "A": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "Ia"
}
result_text = ''
text = input()
for letter in text:
    if letter in alphabet:
        result_text += alphabet.get(letter)
    elif letter.upper() in alphabet and letter.islower():
        result_text += alphabet.get(letter.upper()).lower()
    elif letter == "ь" or letter == "ъ":
        continue
    else:
        result_text += letter
print(result_text)
