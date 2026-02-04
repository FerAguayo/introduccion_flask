from flask import Flask, render_template

#Iniciamos la variable app con Flask
app = Flask(__name__)

@app.route("/hola")
def hola_mundo():
    return "Hola Mundo Flask"

@app.route("/frutas")
def list_frutas():
    list_fruta = ["platano","fresa","piña","uva","melon"]
    return list_fruta

@app.route("/diccionario")
def list_dic():
    dic = [{"name": "Maria","email":"maria@email.com"},{"name": "Carlos","email":"carlos@email.com"}]
    return dic
#pasar parametro por ruta url
app.route("/nombre/<name>")
def tu_nombre(name):
    return f"Hola {name}, cómo estás?"

@app.route("/num/<parametro>")
def cuadrado(parametro):
    parametro = int(parametro)
    return f"el cuadrado de {parametro} es {parametro*parametro}"

#Ejercicio: Realizar una ruta que dinámicamente pueda solicitar o realizar
#operaciones mataematicas de suma, resta, multiplicacion y division
#debe ingresar dos parametros numericos y la operacion a realizar

@app.route("/calculador/<int:num1>/<int:num2>/<op>")
def operaciones_mates(num1,num2,op):
    result = ""
    if op == "suma":
        result = f"La suma es: {num1+num2}"
    elif op == "resta":
        result = f"La suma es: {num1-num2}"
    elif op == "multi":
        result = f"La suma es: {num1*num2}"
    elif op == "divi":
        result = f"La suma es: {num1/num2}"
    return result

@app.route("/html")
def mi_html():
    return render_template("hola.html", variable = "Hola, esto es una variable desde el método", nombre ="Fer")

@app.route("/segunda")
def mi_html_segunda():
    return render_template("segunda.html")

#Al método operaciones matres agregamos una vista html y mostramos dentro de esta 
#su resultado y los numeros y la operacion
#si el usuario no para una operacion mostrar un mensaje debe ingresar operacion
@app.route("/calculadora/<int:num1>/<int:num2>/<op>")
def operaciones_mates_tarea(num1,num2,op):
    result = ""
    if op == "suma":
        result = f"La suma es:{num1} + {num2} = {num1+num2}"
    elif op == "resta":
        result = f"La suma es: {num1} - {num2} = {num1-num2}"
    elif op == "multi":
        result = f"La suma es: {num1} * {num2} = {num1*num2}"
    elif op == "divi":
        result = f"La suma es: {num1} / {num2} = {num1/num2}"
    else:
        result = "Debe ingresar un comando de operación (suma,resta,multi o divi)"
    return render_template("tarea.html", resultado = result)