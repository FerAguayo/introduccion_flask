from flask import Flask
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

