"""
Author(s): Nathanael Ogden
Date: 11/11/2026
this file makes the training and test data files. 
"""
import requests
#main

#helper functions
def find_generation(pokemon_id):
    """
    this finds the generation number for a given pokemon
    pokemon_id: the id of the pokemon as a string.
    returns a string representing the generation number.
    """
    #make a request for the pokemon's data and use the requests json method to turn it into a dictionary.
    pokemon=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon_id+"/")
    pokemon_data=pokemon.json()
    #find the first game the pokemon was in
    pokemon_first_game=pokemon_data["game_indices"][0]["version"]["name"]
    pokemon_first_game=pokemon_first_game.lower()
    #based on what game this is, return the generation it is in.
    if pokemon_first_game=="red" or pokemon_first_game=="blue" or pokemon_first_game=="yellow":
        return "1"
    elif pokemon_first_game == "gold" or pokemon_first_game == "silver" or pokemon_first_game == "crystal":
        return "2"
    elif pokemon_first_game == "ruby" or pokemon_first_game == "sapphire" or pokemon_first_game == "emerald" or pokemon_first_game == "firered" or pokemon_first_game == "leafgreen":
        return "3"
    elif pokemon_first_game=="diamond" or pokemon_first_game=="pearl" or pokemon_first_game=="platinum" or pokemon_first_game=="heartgold" or pokemon_first_game=="soulsilver":
        return "4"
    elif pokemon_first_game=="black" or pokemon_first_game=="white" or pokemon_first_game=="black-2" or pokemon_first_game=="white-2":
        return "5"
    elif pokemon_first_game=="x" or pokemon_first_game=="y" or pokemon_first_game=="alpha-sapphire" or pokemon_first_game=="omega-ruby":
        return "6"
    elif pokemon_first_game=="sun" or pokemon_first_game=="moon" or pokemon_first_game=="ultra-sun" or pokemon_first_game=="ultra-moon":
        return "7"
    elif pokemon_first_game=="sword" or pokemon_first_game=="sheild" or pokemon_first_game=="legends-arceus":
        return "8"
    else:
        return "9"
    
def find_usable_base_stats(pokemon_id):
    """
this finds the usable base stats, or the pokemon's base stats minus lower attacking stat.
pokemon_id: a string representing the id of the pokemon
returns an int representing the base stats
    """
    #make a request for the pokemon and get the list of stats
    pokemon=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon_id+"/")
    pokemon_stats=pokemon.json()["stats"]
    #create a list for the base stats and use a for loop to get the base stats into a list.
    pokemon_base_stats=[]
    for i in range(len(pokemon_stats)):
        pokemon_base_stats.append(pokemon_stats[i]["base_stat"])
    if pokemon_base_stats[1]>=pokemon_base_stats[3]:
        return sum(pokemon_base_stats)-pokemon_base_stats[3]
    else:
        return sum(pokemon_base_stats)-pokemon_base_stats[1]
