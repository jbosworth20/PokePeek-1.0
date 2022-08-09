import flask
from api import *
#Flask
app = flask.Flask(__name__)
#The homepage
@app.route('/')
def home():
    return flask.render_template('index.html')
#What goes on when the user clicks the search button
@app.route("/search", methods = ['POST', 'GET'])
def search():
    if flask.request.method == "POST":
        pokemon_name = flask.request.form['search']
        pokemon = api(pokemon_name)
        pokemon_info = pokemon.get_pokemon()
        pokemon_name = pokemon.get_name(pokemon_info)
        return flask.redirect(flask.url_for('pokemon',name = pokemon_name))
    return flask.render_template('index.html')

#The pokemon name route for the search
@app.route("/pokemon/<name>")
def pokemon(name):
    return flask.render_template('pokemon.html',name = name)
if __name__ == '__main__':
    app.run(debug = True)

