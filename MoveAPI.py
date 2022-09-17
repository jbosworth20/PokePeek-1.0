import requests
from flask import *
class MoveAPI:
    def __init__(self,move_name):
            self.move_name = move_name
    
    def get_move_info(self): 
        link = "https://pokeapi.co/api/v2/move/" + self.move_name #issue is with move_name is literally move_name
        print(link)
        move_response = requests.get(link)
        json = move_response.json()
        move_info = {
            "name":  self.move_name,
            "description": json.get("effect_entries")[0].get('effect'),
            "accuracy": json.get("accuracy"),
            "power": json.get("power"),
            "pp": json.get("pp"),
            "type": json.get("type").get("name")
            }
        return move_info