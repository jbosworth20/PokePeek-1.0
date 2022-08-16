from flask import *
from api import *
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
        pokemon = api(pokemon_name)
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
    api_ = api(name)
    json = api_.get_pokemon()
    pokemon_info = []
    pokemon_name = api_.get_name(json)
    pokemon_type = api_.get_types(json)
    pokemon_stats = api_.get_stats(json)
    pokemon_abilities = api_.get_abilities(json)
    #pokemon_moves = api_.get_moves(json) <- Get this to work
    pokemon_sprite = api_.get_sprite(json)
    pokemon_info.extend([pokemon_name,pokemon_type,pokemon_stats,pokemon_abilities,pokemon_sprite])
    return render_template('pokemon.html',name = pokemon_info[0],data = pokemon_info) #issue is with html not this


@app.route("/error",  methods = ['POST', 'GET'])
def error():
    try:
        pokemon_name = request.form['search']
        pokemon = api(pokemon_name)
        pokemon_info = pokemon.get_pokemon()
        pokemon_name = pokemon.get_name(pokemon_info)
        return redirect(url_for('pokemon',name = pokemon_name))
    except:
        return render_template("error.html")

if __name__ == '__main__':
    app.run(debug = True)
