# Introdución a Flask

Programa hecho en python con el framework Flask

# Instalación

-Crear un entorno en python, actívalo y ejecutar el comando
```
pip install -r requirements.txt
```
La librería utilizada es https://flask.palletsprojects.com/en/stable/

# Iniciando en server flask

Para iniciar el servidor flask tendremos que hacer lo siguiente dependiendo de la plataforma:

-En cmd o powershell desde windows:

```set FLASK_APP=main.py```

-Desde la terminal de comandos de mac o linux:

```export FLASK_APP=main.py```

Una vez exportado el parámetro debemos ejecutar el servidor:

```flask --app main run```

## IMPORTANTE:
Esto es un servidor de desarrollo, por favor no utilizarlo en producción.

