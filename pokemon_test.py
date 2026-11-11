import requests
import json
pokemon=requests.get("https://pokeapi.co/api/v2/pokemon/1/")
print(pokemon.json())
pokemon_file=open("okemon.txt","w")

pokemon_file.write(pokemon.json())