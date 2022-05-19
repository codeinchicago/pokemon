"""
Pokemon API Wrapper
Create a python wrapper for the Pokemon API. It should take in a pokemon name and display the pokemon with its height and weight
"""

#To do:
# Deal with input of wrong Pokemon name/errors in input.

import requests

def pokefinder(rodent):
    lookup = requests.get(f"https://pokeapi.co/api/v2/pokemon/{rodent}")

    data = lookup.json()
    height = data['height']
    print(f"This pokemon is {height} centimeters tall.")

    weight = data['weight']
    print(f"This pokemon weighs {weight} grams.")

pokefinder("squirtle")