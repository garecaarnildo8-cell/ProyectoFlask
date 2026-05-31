from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")

def inicio():
    return "Hola mundo desde mi primera API"

@app.route("/saludo")

def saludo():
    return "Bienvenido a mi API"

@app.route("/usuario")

def usuario():
    return jsonify({
        "nombre": "Arnildo",
        "edad": 20,
        "carrera": "Ingenieria Informatica"
    })

if __name__ =="__main__":
    app.run(debug=True)
