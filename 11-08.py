text = input()
print(text[text.find("?q=") + 3:text.find("&")])
