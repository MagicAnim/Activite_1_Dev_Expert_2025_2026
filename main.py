# Flask : Classe principale, initialise l'app
# render_template : Charge et compile les templates Jinja2
# session : Stockage côté serveur des données utilisateur
# request : Accès aux données de la requête HTTP
# url_for : Génération dynamique des URLs
# redirect : Redirection HTTP vers une autre route

# On importe mongodb, os, bcrypt (chiffrement des mdps)
import pymongo, os, bcrypt
# On import du framework flask :
# * la classe Flask
# * render_template fonction qui permet d'afficher un fichier HTML
from flask import Flask, render_template, session, request, url_for, redirect
# On crée une variable qui stocke une instance de la classe Flask
app = Flask(__name__)

# On crée une clef de chiffrement -> obligatoire pour utiliser session => elle signe et chiffre les cookies
# On crée une valeur au hasard de 24 bits
app.secret_key = os.urandom(24)

# Connexion database
mongo = pymongo.MongoClient("mongodb+srv://magicsecours02_db_user:TcUd6j6J1vIhzy3a@cluster0.zff4fzk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# On crée un route de notre page d'accueil
@app.route('/')
def index():
    # On récupère la collection annonces de notre base de données
    db_annonces = mongo.db.annonces
    annonces =  db_annonces.find({})
    return render_template("index.html", annonces = annonces)

# On crée le route pour l'inscription de l'utilisateur
@app.route('/register', methods = ['GET', 'POST'] )
def register():
    
    return render_template("register.html")


# On teste notre base de données
@app.route('/test')
def test():
    db_test = mongo.db.test
    test = db_test.find({})
    return render_template("test.html", test=test)

# On exécute de notre application flask à laquelle on accède via le port 4200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 4200)