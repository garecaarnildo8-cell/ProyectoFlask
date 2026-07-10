from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    datos = request.get_json()
    datos["id"] = len(usuarios)
    usuarios.append(datos)
    return jsonify({"Mensaje":"Creado exitosamente"}), 201

@app.route("/usuarios/<id>", methods=["PUT"])
def actualizar_usuario(id):
    for i in usuarios:
        if i["id"]==int(id):
            datos = request.get_json()
            i["nombre"] = datos["nombre"]
            i["correo"] = datos["correo"]
            
            return jsonify({"Mensaje":"Usuario modificado exitosamente"}), 200
@app.route("/usuarios/<id>", methods=["DELETE"])
def eliminar_usuario(id):
    for i in usuarios:
        if i["id"]==int(id):
            usuarios.remove(i)
            return jsonify({"Mensaje":"Usuario eliminado exitosamente"}), 200
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)