"""
Author(s): Nathanael Ogden
Date: 11/11/2026
this file makes the training and test data files. 
"""
import requests


#helper functions
def find_generation(pokemon_id):
    """
    this finds the generation number for a given pokemon
    pokemon_id: the id of the pokemon as a string.
    returns a string representing the generation number.
    """
    #make a request for the pokemon's data and use the requests json method to turn it into a dictionary.
    pokemon=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon_id+"/")
    pokemon_data=pokemon.json
    #find the first game the pokemon was in
    pokemon_first_game=pokemon_data["game_indices"][0]["version"]["name"]
    pokemon_first_game=pokemon_first_game.lower()
    #based on what game this is, return the generation it is in.
    if pokemon_first_game=="red" or pokemon_first_game=="blue" or pokemon_first_game=="yellow":
        return "1"
    
pokemon_versions=requests.get("https://pokeapi.co/api/v2/version/")
print(pokemon_versions.json())