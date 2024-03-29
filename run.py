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
        pokemon = PokemonAPI(request.form['search'])
        json_ = pokemon.get_pokemon()
        pokemon_name = pokemon.get_name(json_)
        if(pokemon.confirm_legit(json_) != '404'):
            return redirect(url_for('pokemon',name = pokemon_name))
        else:
            return redirect(url_for('error'))
    return render_template('home.html')

#The pokemon name route for the search
@app.route("/<name>")
def pokemon(name): #Make the pokemon api parts better
    if request.method == "GET":
        api = PokemonAPI(name)
        json = api.get_pokemon()
        pokemon_info = api.get_all_info(json)
        return render_template('pokemon.html',name = pokemon_info[0],data = pokemon_info) #issue is with html not this

@app.route("/get_moves", methods = ['POST'])
def get_moves():
    if request.method == "POST": 
        pokemon_name = request.form['pokemon']
        move_name = request.form['move'].lower()
    return redirect(url_for('move',name = pokemon_name,move = move_name))
@app.route("/<name>/<move>", methods = ['POST','GET']) #To get this to show up - try rendering page with pokemon_api call info for name and also tack on move_info
def move(name,move):
    api = PokemonAPI(name)
    json = api.get_pokemon()
    pokemon_info = api.get_all_info(json)
    api = MoveAPI(move) 
    move_info = api.get_move_info()
    pokemon_info.extend(move_info)
    return render_template('pokemon.html',name = pokemon_info[0],move = pokemon_info[6], data = pokemon_info)
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
