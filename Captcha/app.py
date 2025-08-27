#Importar la biblioteca de flask
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicilizar la aplicacion
#1. nombre por defecto
#2. ruta donde esta los templates o nombre de la carpeta
app = Flask(__name__, template_folder='templates')

#Clave secreta de la aplicacion
app.secret_key = '123456789'

#Controlador de la ruta por defecto
@app.route('/')
def index():
    return render_template('index.html')

#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)