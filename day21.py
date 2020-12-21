with open('inputs/day21.txt') as f:
    foods = [line.strip() for line in f.readlines()]

allergen_to_ingredient = dict()
ingredients_set = set()
count_ingredients = dict()
for food in foods:
    ingredients, allergens = food.split('(')
    ingredients = ingredients.split()
    allergens = allergens[9:-1].split(', ')

    for a in allergens:
        if a not in allergen_to_ingredient:
            allergen_to_ingredient[a] = set(ingredients)
        else:
            allergen_to_ingredient[a] = allergen_to_ingredient[a].intersection(set(ingredients))
    ingredients_set = ingredients_set.union(set(ingredients))
    for i in ingredients:
        count_ingredients[i] = count_ingredients.get(i, 0) + 1

count = 0
possibly_allergen = {ing for ings in allergen_to_ingredient.values() for ing in ings}
for ing in ingredients_set:
    if ing not in possibly_allergen:
        count += count_ingredients[ing]
# Part 1
print(count)

ingredient_to_allergen = dict()
while len(allergen_to_ingredient) != 0:
    for a, ing_set in allergen_to_ingredient.items():
        if len(ing_set) == 1:
            remove_ing = ing_set.pop()
            ingredient_to_allergen[remove_ing] = a
            del allergen_to_ingredient[a]
            break
    for a, ing_set in allergen_to_ingredient.items():
        if remove_ing in ing_set:
            allergen_to_ingredient[a].remove(remove_ing)

ingredient_list = [(i, a) for i, a in ingredient_to_allergen.items()]
ingredient_list.sort(key=lambda t: t[1])
# Part 2
print(','.join(x[0] for x in ingredient_list))