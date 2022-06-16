names_1 = set()
names_2 = set()
recipe = set()
M = int(input())
for i in range(M):
    product_name1 = input()
    names_1.add(product_name1)
N = int(input())
for j in range(N):
    recipe_name = input()
    recipe.add(recipe_name)
    product_count = int(input())
    for k in range(product_count):
        product_name2 = input()
        names_2.add(product_name2)
    if product_name2 in names_1:
        print(recipe_name)

