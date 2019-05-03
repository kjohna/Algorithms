#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    lowest = float("Inf")
    for key in recipe:
        # if we don't have the req'd ingredient, ans is 0
        if not key in ingredients:
            return 0
        # how many whole batches can we make based on curr ingredient?
        make_max = ingredients[key] // recipe[key]
        if make_max < lowest:
            # store that number if it is lower than current min
            lowest = make_max
    return lowest


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
