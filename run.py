from flask import *
from api import *
#Flask
app = Flask(__name__)
#The homepage
@app.route('/')
def home():
    return render_template('home.html')
#What goes on when the user clicks the search button
@app.route("/search", methods = ['POST', 'GET'])
def search():
    if request.method == "POST":
        pokemon_name = request.form['search']
        pokemon = api(pokemon_name)
        pokemon_info = pokemon.get_pokemon()
        pokemon_name = pokemon.get_name(pokemon_info)
        return redirect(url_for('pokemon',name = pokemon_name))
    return render_template('home.html')

#The pokemon name route for the search
@app.route("/pokemon/<name>")
def pokemon(name):
    return render_template('pokemon.html',name = name)
if __name__ == '__main__':
    app.run(debug = True)

