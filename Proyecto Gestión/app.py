#Importar la biblioteca de flask
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicilizar la aplicacion
#1. nombre por defecto
#2. ruta donde esta los templates o nombre de la carpeta
app = Flask(__name__, template_folder='templates')

usuarios =[]
listaPostres = []
listaBebidas=[]
listaSnacks=[]
listaComidas=[]

#Clave secreta de la aplicacion
app.secret_key = '123456789'

#Controlador de la ruta por defecto
@app.route('/')
def index():
    return render_template('login.html',usuarios=usuarios)

@app.route('/enviar',methods=["GET","POST"])
def enviarDatos():
    
    email=request.form.get("email")
    password=request.form.get("password")
    

    if request.method =="GET":
        return render_template("agregar.html")
    else:   
            data=[
                    email,
                    password
                 ]
            
            usuarios.append(data)
            return redirect("/")

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/acerca-nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/snacks')
#Función inicio que llamara a nuestra página snacks
def snacks():
    return render_template('snacks.html', lsnacks = listaSnacks)
#controlador para ingresar datos en comestibles
@app.route('/ingresar_snacks', methods=['GET','POST'])
def ingresar_snacks():
    if(request.method == "POST"):
        productos_cm = request.form['producto_cm']
        cantidades_cm = request.form['cantidad_cm']
        listaSnacks.append({'producto_cm': productos_cm,'cantidad_cm': cantidades_cm })
        return redirect(url_for('snacks'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_snacks', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_snacks():
    if(request.method == "POST"):
        listaSnacks.clear()
        return redirect(url_for('snacks'))

@app.route('/bebidas')
#Función inicio que llamara a nuestra página bebidas
def bebidas():
    return render_template('bebidas.html', lbebidas = listaBebidas)
#controlador para ingresar datos en comestibles
@app.route('/ingresar_bebidas', methods=['GET','POST'])
def ingresar_bebidas():
    if(request.method == "POST"):
        productos_cm = request.form['producto_cm']
        cantidades_cm = request.form['cantidad_cm']
        listaBebidas.append({'producto_cm': productos_cm,'cantidad_cm': cantidades_cm })
        return redirect(url_for('bebidas'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_bebidas', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_bebidas():
    if(request.method == "POST"):
        listaBebidas.clear()
        return redirect(url_for('bebidas'))


@app.route('/postres')
#Función inicio que llamara a nuestra página postres
def postres():
    return render_template('postres.html', lpostres = listaPostres)
#controlador para ingresar datos en comestibles
@app.route('/ingresar_postres', methods=['GET','POST'])
def ingresar_postres():
    if(request.method == "POST"):
        productos_cm = request.form['producto_cm']
        cantidades_cm = request.form['cantidad_cm']
        listaPostres.append({'producto_cm': productos_cm,'cantidad_cm': cantidades_cm })
        return redirect(url_for('postres'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_postres', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_postres():
    if(request.method == "POST"):
        listaPostres.clear()
        return redirect(url_for('postres'))


@app.route('/comidas')
#Función inicio que llamara a nuestra página comidas
def comidas():
    return render_template('comidas.html', lcomidas = listaComidas)
#controlador para ingresar datos en comestibles
@app.route('/ingresar_comidas', methods=['GET','POST'])
def ingresar_comidas():
    if(request.method == "POST"):
        productos_cm = request.form['producto_cm']
        cantidades_cm = request.form['cantidad_cm']
        listaComidas.append({'producto_cm': productos_cm,'cantidad_cm': cantidades_cm })
        return redirect(url_for('comidas'))
#Controlador para borrar los productos de la lista
@app.route('/borrar_comidas', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar_comidas():
    if(request.method == "POST"):
        listaComidas.clear()
        return redirect(url_for('comidas'))


#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)