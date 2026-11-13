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

def find_type_string(pokemon_id):
    """
    this finds the string of features for the different types a pokemon an have.
    pokemon_id: a string representing the id of the pokemon
    returns a string of yes and no for whether is the pokemon is each type.
    """
    #get the pokemon data and make a list of the pokemon's type, then the get the list of all of the possible types for a pokemon also as a list.
    pokemon=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon_id+"/")
    pokemon_data=pokemon.json()
    pokemon_primary_type=pokemon_data["types"][0]["type"]["name"]
    if len(pokemon_data["types"])>1:
        pokemon_secondary_type=pokemon_data["types"][1]["type"]["name"]
    else:
        pokemon_secondary_type=""
    pokemon_types=[pokemon_primary_type,pokemon_secondary_type]
    possible_pokemon_types=requests.get("https://pokeapi.co/api/v2/type/").json()["results"]
    type_string=" "
    #use a for loop to see if the type is in the list of types for the given pokemon.
    for i in range(len(possible_pokemon_types)):
        if possible_pokemon_types[i]["name"]==pokemon_types[0] or possible_pokemon_types[i]["name"]==pokemon_types[1]:
            if i==0:
                type_string=type_string+"yes"
            else:
                type_string=type_string+" yes"
        else:
            if i==0:
                type_string=type_string+"no"
            else:
                type_string=type_string+" no"
    return type_string

def find_stats_mean():
    """
    this finds the means of the of each stat of the pokemon
    this returns a list of the means..
    """
    #create a list for the value of each stat
    pokemon_stats_list=[0,0,0,0,0,0]
    #use a for loop to get the total for each stat.
    for i in range(1025):
        pokemon=requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i+1)+"/")
        for j in range(len(pokemon_stats_list)):
            pokemon_stats_list[j]=pokemon_stats_list[j]+pokemon.json()["stats"][j]["base_stat"]
    #use a for loop to divide each value by the number of pokemon
    for i in range(len(pokemon_stats_list)):
        pokemon_stats_list[i]=pokemon_stats_list[i]/1025
    return pokemon_stats_list
def find_attacking_difference(pokemon_id):
    """
    this finds the difference in a pokemon's attacking stats to see how much they lean toward one or the other.
    pokemon_id: a string representing the 
 id of the pokemon
     returns a float representing the difference in the two attacking stats   
       """
    pokemon=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon_id+"/")
    return abs(pokemon.json()["stats"][1]["base_stat"]-pokemon.json()["stats"][3]["base_stat"])

def find_stat_difference(stat_mean,pokemon_id):
    """
    find the difference from the mean in each base stat for a pokemon
    stat_mean: a list for the stat means of the pokemon
    pokemon_id: a string representing the id of the pokemon
    returnn a float representing the total difference of a pokemon's base stats. 
    """
    pokemon=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon_id+"/")
    base_stat_difference=0
    for i in range(len(stat_mean)):
        base_stat_difference=base_stat_difference+(pokemon.json()["stats"][i]["base_stat"]-stat_mean[i])
    return base_stat_difference

def create_pokemon_files():
    """
    this create the test and training data files.
    returns nothing but created files
    """
    return
