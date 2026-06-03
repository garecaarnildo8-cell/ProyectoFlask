from flask import Flask, jsonify, request
import psycopg2 

def conectar():
    return psycopg2.connect(
        host = "localhost",
        database="apiusuarios",
        user= "postgres",
        password= "1234"
    )
    
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

#GET usuarios desde base de datos
@app.route("/db/usuarios", methods=["GET"])
def obtener_usuarios_db():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios")
    filas = cur.fetchall()
    cur.close()
    conn.close()
    
    usuarios_db = []
    for fila in filas:
        usuarios_db.append({
            "id": fila[0],
            "nombre": fila[1],
            "edad": fila[2]
        })
    
    return jsonify(usuarios_db)

#Agregar ususarios a la base de datos metodo POST

@app.route("/db/usuarios", methods=["POST"])
def agregar_usuarios_db():
    conn = conectar()
    cur= conn.cursor()
    
    dato = request.get_json()
    nombre = dato["nombre"]
    edad = dato["edad"]
    
    cur.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({
        "Mensaje " : f"Usuario {nombre} registrado exitosamente"
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

#metodo GET buscar un usuario - ID
@app.route("/usuarios/<int:numero>")

def buscar_usuario(numero):
    
    for i in  usuarios:
        if i["id"] == numero:
            return jsonify(i)
          
    return jsonify({"error": "Usuario no encontrado"}), 404   

#Metodo POST agregar un usuario
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

#Actualizar los datos del usuario metodo PUT por parametro

@app.route("/usuarios/<int:numero>", methods=["PUT"])

def actualizar_datos(numero): 
    datos=request.get_json()

    for i in usuarios: 
        if i["id"] == numero:
            i["nombre"] = datos["nombre"]
            i["edad"] = datos["edad"]
            return jsonify(i)

    return jsonify({"error": "Usuario no encontrado"}), 404   

#Eliminar un usuario con parametrp metodo DELETE

@app.route("/usuarios/<int:numero>", methods=["DELETE"])

def Eliminar_Usuario(numero): 
    for i in usuarios: 
        if i["id"]==numero: 
            usuarios.remove(i)

            return jsonify({
                "Mensaje" : f"Usuario {i['nombre']} eliminado exitosamente"
            })
            
    return jsonify({"error": "Usuario no encontrado"}), 404 
 
if __name__ =="__main__":
    app.run(debug=True)
