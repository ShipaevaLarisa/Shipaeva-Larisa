number = int(input())
soup = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
for i in range(number):
    print(soup[i % 5])
