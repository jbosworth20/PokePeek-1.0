from flask import *
from PokemonAPI import *
from MoveAPI import *

#Flask
app = Flask(__name__)
pokemon_info = []
#The homepage
@app.route('/')
def home():
    return render_template('home.html')
#What goes on when the user clicks the search button
@app.route("/search", methods = ['POST', 'GET'])
def search(): #This method is terrible - make it better in terms of making it simple and less weird
    if request.method == "POST": 
        pokemon_name = request.form['search']
        pokemon = PokemonAPI(pokemon_name)
        json_ = pokemon.get_pokemon()
        pokemon_name = pokemon.get_name(json_)
        if(pokemon.confirm_legit(json_) != '404'):
            return redirect(url_for('pokemon',name = pokemon_name))
        else:
            return redirect(url_for('error'))
    return render_template('home.html')

#The pokemon name route for the search
@app.route("/pokemon/<name>")
def pokemon(name): #Make the pokemon api parts better
    if request.method == "GET":
        api = PokemonAPI(name)
        json = api.get_pokemon()
        pokemon_info = []
        pokemon_name = api.get_name(json) #0
        pokemon_sprite = api.get_sprite(json)#1
        pokemon_type = api.get_types(json)#2
        pokemon_stats = api.get_stats(json)#3
        pokemon_abilities = api.get_abilities(json)#4
        pokemon_moves = api.get_move_names(json) #5
        pokemon_info.extend([pokemon_name,pokemon_sprite,pokemon_type,pokemon_stats,pokemon_abilities,pokemon_moves])
    return render_template('pokemon.html',name = pokemon_info[0],data = pokemon_info) #issue is with html not this

@app.route("/move", methods = ['POST','GET']) #To get this to show up - try rendering page with pokemon_api call info for name and also tack on move_info
def move():
    pokemon_name = request.form['pokemon']
    api = PokemonAPI(pokemon_name)
    json = api.get_pokemon()
    pokemon_info = []
    pokemon_name = api.get_name(json) #0
    pokemon_sprite = api.get_sprite(json)#1
    pokemon_type = api.get_types(json)#2
    pokemon_stats = api.get_stats(json)#3
    pokemon_abilities = api.get_abilities(json)#4
    pokemon_moves = api.get_move_names(json) #5
    move_name = request.form['move'] .lower()
    pokemon_info.extend([pokemon_name,pokemon_sprite,pokemon_type,pokemon_stats,pokemon_abilities,pokemon_moves])
    api = MoveAPI(move_name) 
    move_info = api.get_move_info()
    move_name = move_info['name'] #6
    move_description = move_info['description'] #7
    move_accuracy = move_info['accuracy'] #8
    move_power = move_info['power'] #9
    move_pp = move_info['pp'] #10
    move_type = move_info['type'] #11
    pokemon_info.extend([move_name,move_description,move_accuracy,move_power,move_pp,move_type])
    return render_template('pokemon.html',name = pokemon_info[0],data = pokemon_info)
    #return move_info #Figure out how to turn this into just data 

@app.route("/error",  methods = ['POST', 'GET'])
def error():
    try:
        pokemon_name = request.form['search']
        pokemon = PokemonAPI(pokemon_name)
        pokemon_info = pokemon.get_pokemon()
        pokemon_name = pokemon.get_name(pokemon_info)
        return redirect(url_for('pokemon',name = pokemon_name))
    except:
        return render_template("error.html")

if __name__ == '__main__':
    app.run(debug = True)
