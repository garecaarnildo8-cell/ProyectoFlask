from flask import Flask
from flask import Flask, jsonify
from flask import Flask, jsonify, request

#GET - BUSCAR
#inicio  
app = Flask(__name__)

usuarios = [
    
    {"id": 1, "nombre": "Juan", "edad": 25},
    {"id": 2, "nombre": "Ana", "edad": 22},
    {"id": 3, "nombre": "Carlos", "edad": 28}
]

@app.route("/")

def inicio():
    return "Hola mundo desde mi primera API"

#Saludo
@app.route("/saludo")

def saludo():
    return "Bienvenido a mi API"


#Datos estaticos - usando json
@app.route("/usuario")

def usuario():
    return jsonify({
        "nombre": "Arnildo",
        "edad": 20,
        "carrera": "Ingenieria Informatica"
    })

#Datos  por parametro - usando json
@app.route("/saluda/<nombre>")

def saludo_personalizado(nombre):
    return jsonify({
        "mensaje" : f"Hola {nombre}, bienvenido a mi API"
    })

#Determinar paridad por parametro - usando json
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
#GET
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(usuarios)

# ruta crear usuario usando POST - usando json
@app.route("/usuario", methods=["POST"])
def crear_usuario():
    datos = request.get_json()
    nombre = datos["nombre"]
    edad = datos["edad"]
    
    return jsonify({
        "Mensaje ": f"Usuario {nombre} creado exitosamente.",
        "edad" : edad
        
    })

@app.route("/usuarios/<int:numero>")

def buscar_usuario(numero):
    
    for i in  usuarios:
        if i["id"] == numero:
            return jsonify(i)
          
    return jsonify({"error": "Usuario no encontrado"}), 404   

@app.route("/nuevousuario", methods=["POST"])

def nuevo_usuario():
    datos = request.get_json()
    nombre = datos["nombre"]
    edad  = datos["edad"]
    nuevoid = len(usuarios)+1
    
    nuevo = {
    "id": nuevoid,
    "nombre": nombre,
    "edad": edad
    }
    
    usuarios.append(nuevo)
    
    return jsonify({
        "Mensaje ": f"Usuario {nombre} creado exitosamente.",
        "usuario ": nuevo
    })

if __name__ =="__main__":
    app.run(debug=True)
