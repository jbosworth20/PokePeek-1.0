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

    def get_moves(self,json):
        possible_moves = {}
        for moves in json["moves"]:
            ind_information = []
            # Name
            move_name = "https://pokeapi.co/api/v2/move/" + \
                moves.get('move').get('name').json()
            move_response = requests.get(move_name)
            # Description
            ind_information.append(move_response.get(
                "effect_entries")[0].get("short_effect"))
            # Accuracy
            ind_information.append(move_response.get("accuracy"))
            # Type
            type_path = "https://pokeapi.co/api/v2/type/" + \
                ind_information.append(move_response.get("type").get("name"))
            # Damage Multiplier
            damage_list = ["double_damage_from", "double_damage_to",
                        "half_damage_from", "half_damage_to", "no_damage_to"]
            damage_types = self.get_damage_multiplier(requests.get(type_path).json()[
                                                "damage_relations"], damage_list)
            ind_information.append(damage_types)
            # NOTE Need from damage types from this array for the pokemon
            possible_moves[move_name] = ind_information
        return possible_moves

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
        print(sprite_link)
        return sprite_link
    
    def confirm_legit(self,json):
        try:
            pokemon_json = self.get_pokemon()
            pokemon_name = self.get_name(pokemon_json)
            return(pokemon_name)
        except:
            return("404")