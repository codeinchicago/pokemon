"""
Pokemon API Wrapper
Create a python wrapper for the Pokemon API. It should take in a pokemon name and display the pokemon with its height and weight
"""

import requests

rodent = input("What pokemon would you like to investigate? ").lower()

def pokefinder():

    lookup = requests.get(f"https://pokeapi.co/api/v2/pokemon/{rodent}")

    if lookup.status_code == 200:
        print("Pokemon found, measuring it.")

    data = lookup.json()
    height = data['height']
    print(f"{rodent.title()} is {height} centimeters tall.")

    weight = data['weight']
    print(f"{rodent.title()} weighs {weight} grams.")

pokefinder()