from flask import Flask
from flask import Flask, jsonify
from flask import Flask, jsonify, request

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

# ruta crear usuario usando POST
@app.route("/usuario", methods=["POST"])
def crear_usuario():
    datos = request.get_json()
    nombre = datos["nombre"]
    edad = datos["edad"]
    
    return jsonify({
        "Mensaje ": f"Usuario {nombre} creado exitosamente.",
        "edad" : edad
        
    })


if __name__ =="__main__":
    app.run(debug=True)
