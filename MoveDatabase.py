from importlib.metadata import metadata
from typing import Any
from sqlalchemy import *
from sqlite3 import *
import requests
from PokemonAPI import *

class DataBase:
    def __init__(self,pokemon_name):
        self.pokemon_name = pokemon_name
    
    def create_table():
        engine = create_engine('sqlite:///moves',echo = true)
        connection = engine.connect()
        metadata = metadata()
        move_info = Table('move_info',metadata,
        Column('move_name',String(255),nullable = False),
        Column('description',String(2000),nullable = False),
        Column('accuracy',Integer()),
        Column('power',Integer()),
        Column('pp',Integer()),
        Column('type',String(255),nullable = False))
        return move_info
    
    def insert_moves(self): #Try to get name from pokemon page and then get individual move info on click and make it a tuple
        move_database = self.create_table(self.pokemon)
        pokemon = PokemonAPI(self.pokemon)
        pokemon_info = pokemon.get_pokemon(self.pokemon)
        move_json = pokemon_info["moves"]
        for i, move in move_json:
            move_info = []
            name = move_json[i].get("move").get("name")
            link = "https://pokeapi.co/api/v2/move/" + name
            move_response = requests.get(link).json()
            #Description
            description = move_response.get("effect_entries")[0].get('effect')
            #Accuracy
            accuracy = move_response.get("accuracy")
            #Power
            power = move_response.get("power")
            #PP
            pp = move_response.get("pp")
            #Type
            type_ = move_response.get("type").get("name")
            move_database.insert(move_info).values(move_name = name,description = description,accuracy = accuracy,power = power,pp = pp,type = type_)
        return move_database
    
    def get_move_info(self,database_name,move_name):
        results = database_name.select([database_name]).where(database_name.columns.move_name == move_name)
        return results

