from flask import Flask
from pymongo import MongoClient
from flask import Flask,render_template,url_for,request, redirect
# para manejar el <id> que viene por la URL 
from bson.objectid import ObjectId

app = Flask(__name__)
# con el localhost 27017 por default no usa username ni password
# client = MongoClient('localhost', 27017)
# si se configura y  la conexion agregando user  modificando mongod.cfg y reiniciando 
client = MongoClient('localhost', 27017, username='Admin1980', password='delcamino333')


# You then use the client instance to create a MongoDB database called flask_db and save a reference to it in a variable called db.
db = client.flask_db

# Then you create a collection called coleccion on the flask_db database using the db variable.
coleccion = db.coleccion

client = MongoClient('localhost', 27017, username='username', password='password')


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        coleccion.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
# para mostrar la COLECCCION 
    all_todos = coleccion.find()
    return render_template('index.html', allColeccion=all_todos)
# esta ruta es una abreviacion de @app.route("/login", methods=["POST"])
@app.post('/<id>/delete/')
def delete(id):
    # objectId se IMPORTO para darle manelo a la ID
    coleccion.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))