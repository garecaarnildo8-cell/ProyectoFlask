import os
os.environ['LANG'] = 'C'

import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="usuariosdb",
        user="postgres",
        password="1234"
    )

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios")
    filas = cur.fetchall()
    cur.close()
    conn.close()
    usuarios = [{"id": f[0], "nombre": f[1], "correo": f[2]} for f in filas]
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    datos = request.get_json()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)",
                (datos["nombre"], datos["correo"]))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"Mensaje": "Usuario creado exitosamente"}), 201

@app.route("/usuarios/<id>", methods=["PUT"])
def actualizar_usuario(id):
    datos = request.get_json()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE usuarios SET nombre=%s, correo=%s WHERE id=%s", (datos["nombre"],datos["correo"],id))    
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"Mensaje": "Usuario modificado exitosamente."}),200

@app.route("/usuarios/<id>", methods=["DELETE"])
def eliminar_usuario(id):
    conn=get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuarios WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"Mensaje": "Usuario eliminado exitosamente."}),200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)