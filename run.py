from flask import *
from api import *
import requests
#Flask
app = Flask(__name__)
#The homepage
@app.route('/')
def home():
    return render_template('index.html')
#What goes on when the user clicks the search button
@app.route("/search", methods = ['POST', 'GET'])
def search():
    if request.method == "POST":
        pokemon_name = request.form['name']
        return redirect(url_for('pokemon',name = pokemon_name))
    return render_template('index.html')

#The pokemon name route for the search
@app.route("/pokemon/<name>")
def pokemon(name):
    return render_template('pokemon.html',name = name)
if __name__ == '__main__':
    app.run(debug = True)

