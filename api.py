import requests
class api:
    def __init__(self,pokemon_name):
        self.pokemon_name = pokemon_name

    def get_pokemon(self):
        name = self.pokemon_name
        if str(name).lower() == "mimikyu":
            full_path = "https://pokeapi.co/api/v2/pokemon/778"
        else:
            full_path = "https://pokeapi.co/api/v2/pokemon/" + str(name).lower()
        response = requests.get(full_path)
        json = response.json()
        return json

    def get_id(self,json):
        id = json["id"]
        return str(id)

    def get_name(self,json):
        if(json["name"] == "mimikyu-disguised"):
            name = "mimikyu"
        else:
            name = json["name"]
        return str(name)

    def get_types(self,json):
        pokemon_types = []
        for types in json["types"]:
            pokemon_types.append(types.get('type').get('name'))
        return pokemon_types

    def get_stats(self,json):
        # 0 = hp 1 = atk 2 = def 3 = sp ak 4 = sp def & 5 = spd_stat
        stat_json = json["stats"]
        stats = []
        for index in range(6):
            stats.append(stat_json[index].get('base_stat'))
        return stats
    
    def get_damage_multiplier(self,damage_response, input_list):
        damages = []
        for damage in input_list:
            damage_type = []
            if damage_response.get(damage):
                for entry in damage_response.get(damage):
                    damage_type.append(entry.get("name"))
                damages.append(damage_type)
        return damages

    def get_moves(self,json): #Try to get name from pokemon page and then get individual move info on click and make it a tuple
        moves = {}
        move_json = json["moves"]
        for i, move in enumerate(move_json,start = 0):
            move_info = []
            #Name
            move_name = move_json[i].get("move").get("name")
            link = "https://pokeapi.co/api/v2/move/" + move_name
            move_response = requests.get(link).json()
            #Description
            description = move_response.get("effect_entries")[0].get('effect')
            print(description)
            move_info.append(description)
            #Accuracy
            accuracy = move_response.get("accuracy")
            move_info.append(accuracy)
            #Power
            power = move_response.get("power")
            move_info.append(power)
            #PP
            pp = move_response.get("pp")
            move_info.append(move_response.get(pp))
            #Type
            type_ = move_response.get("type").get("name")
            move_info.append(type_)
            moves[move_name] = move_info
        return moves
        
    def get_move_info(self, move_name): #Use this method by getting name from get_moves and then finding the key = move and then grabbing move_info
        move = {}
        move_info = []
       

    def get_abilities(self,json):
        abilities = {}
        for ability in json["abilities"]:
            ability_name = ability.get('ability').get('name')
            description_path = "https://pokeapi.co/api/v2/ability/" + ability_name
            description_response = requests.get(description_path).json()
            possible_abilities = list(description_response['effect_entries'])
            for ability in possible_abilities:
                if 'en' in ability.get('language').get('name'):
                    abilities[ability_name] = ability.get('short_effect')
        return abilities

    def get_sprite(self,json):
        id_ = self.get_id(json)
        if(len(id_) == 1):
            id_ = "00" + id_
        elif(len(id_) == 2):
            id_ = "0" + id_
        sprite_link = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + \
            id_ + ".png"
        return sprite_link
    
    def confirm_legit(self,json):
        try:
            pokemon_json = self.get_pokemon()
            pokemon_name = self.get_name(pokemon_json)
            return(pokemon_name)
        except:
            return("404")
