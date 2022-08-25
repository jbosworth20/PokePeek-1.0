from importlib.metadata import metadata
from typing import Any
from sqlalchemy import *
from sqlite3 import *
import requests
from PokemonAPI import *
from pandas import *

class MoveDataBase:
    def __init__(self,pokemon_name):
        self.pokemon_name = pokemon_name
    def get_info(self,move):
        move_info = []
        name = move
        move_info.append(name)
        link = "https://pokeapi.co/api/v2/move/" + name
        move_response = requests.get(link).json()
        #Description
        description = move_response.get("effect_entries")[0].get('effect')
        move_info.append(description)
        #Accuracy
        accuracy = move_response.get("accuracy")
        move_info.append(accuracy)
        #Power
        power = move_response.get("power")
        move_info.append(power)
        #PP
        pp = move_response.get("pp")
        move_info.append(pp)
        #Type
        type_ = move_response.get("type").get("name")
        move_info.append(type_)
    def insert_moves(self): #Try to get name from pokemon page and then get individual move info on click and make it a tuple
        metadata = MetaData()
        moves = Table('moves',metadata,
        Column('move_name',String(255),nullable = False),
        Column('description',String(2000),nullable = False),
        Column('accuracy',Integer()),
        Column('power',Integer()),
        Column('pp',Integer()),
        Column('type',String(255),nullable = False))
        engine = create_engine('sqlite:///moves')
        connection = engine.connect()
        pokemon = PokemonAPI(self.pokemon_name)
        pokemon_info = pokemon.get_pokemon()
        move_json = pokemon_info["moves"]
        for i, move in enumerate(move_json,start = 0):
            name = move_json[i].get("move").get("name")
            move_info = self.get_info(name)
            #insert(moves).values(move_name = name,description = description,accuracy = accuracy,power = power,pp = pp,type = type_)
        dataframe = read_sql_table('moves',engine) 
        return dataframe
    
    def get_move_info(self,database_name,move_name):
        results = database_name.select([database_name]).where(database_name.columns.move_name == move_name)
        return results

