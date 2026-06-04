from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="apiusuarios",
        user="postgres",
        password="1234"
    )

#Obtener datos del usuario base de datos

@app.route("/db/usuarios")
def obtener_usuarios():
    conn= conectar()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM usuarios")
    fila =cur.fetchall()
    cur.close()
    conn.close()
    
    usuarios_db = []
    
    for i in fila:
        usuarios_db.append({
            "id" : i[0],
            "nombre": i[1],
            "edad": i[2]
        })
    return jsonify(usuarios_db)


@app.route("/db/usuarios",methods=["POST"])
def agregar_usuario():
    conn = conectar()
    cur = conn.cursor()
    datos= request.get_json()
    
    nombre= datos["nombre"]
    edad = datos["edad"]

    cur.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({
        "Mensaje " : f"Usuario {nombre} registrado exitosamente"
    })

@app.route("/db/usuarios/<int:numero>", methods=["PUT"])
def actualizar_datos(numero):
    conn=conectar()
    cur = conn.cursor()

    datos = request.get_json()
    nombre = datos["nombre"]
    edad = datos["edad"]
    
    cur.execute("UPDATE usuarios SET nombre=%s, edad=%s WHERE id=%s",(nombre,edad,numero))
    
    if cur.rowcount==0:
        return jsonify({
                "Mensaje" : "Error usuario no encontrado",
        }), 404
    
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({
        "Mensaje": f"Usuario {nombre} registrado exitosamente"
    })
    
@app.route("/db/usuarios/<int:numero>", methods=["DELETE"])

def eliminar_usuario(numero):
    conn = conectar()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM usuarios WHERE id=%s", (numero,))
    
    if cur.rowcount==0:
        return jsonify({"error": "Usuario no encontrado"}),404
    
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({
        "Mensaje": f"usuario {numero} eliminado exitosamente"
    })
if __name__ == "__main__":
    app.run(debug=True)
    
