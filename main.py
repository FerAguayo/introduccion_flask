from flask import Flask
#Iniciamos la variable app con Flask
app = Flask(__name__)

#Inicializar parámetro en el servidor Flask
#En mac:
#export FLASK_APP=main.py
#En pc:
#set FLASK_APP=main.py

#comando para ejecutar el servidor
#flask --app main run

@app.route("/hola")
def hola_mundo():
    return "Hola Mundo Flask"