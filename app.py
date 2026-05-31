from flask import Flask
from flask import Flask, jsonify

#inicio  
app = Flask(__name__)

@app.route("/")

def inicio():
    return "Hola mundo desde mi primera API"


#Saludo
@app.route("/saludo")

def saludo():
    return "Bienvenido a mi API"


#Datos estaticos
@app.route("/usuario")

def usuario():
    return jsonify({
        "nombre": "Arnildo",
        "edad": 20,
        "carrera": "Ingenieria Informatica"
    })


#Datos  por parametro
@app.route("/saluda/<nombre>")

def saludo_personalizado(nombre):
    return jsonify({
        "mensaje" : f"Hola {nombre}, bienvenido a mi API"
    })

#Determinar paridad por parametro
@app.route("/paridad/<int:numero>")

def paridad(numero): 
    if numero%2==0:
        resultado="Par"
    else :
        resultado= "Impar"
    
    return jsonify({
        "numero": numero,
        "resultado": resultado
    })  

if __name__ =="__main__":
    app.run(debug=True)
