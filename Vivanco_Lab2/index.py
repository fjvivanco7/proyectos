#Se importa la librería Flask
from flask import Flask, abort, render_template, request, redirect

#variable de instancia app
app=Flask(__name__)

tareas = []

#Ruta raíz
@app.route('/')

#Ruta página del primer html index
@app.route('/index')

@app.route('/agregar', methods=["GET", "POST"])
def agregar():
    if request.method == "GET":
        return render_template("agregar.html")
    else:
        tarea = request.form.get("tarea")
        tareas.append(tarea)
        return redirect("/inicio")

#función que retorna la página
def inicio():
    return render_template('index.html', tareas=tareas)
