from flask import Flask, jsonify

app = Flask("patito")

def ejemplo(x="a",y="b",z="c"):
    print(x)

@app.route('/json', methods=['GET'])
def ejemplo_json():
    contenido = {"id": 1, "nombre": "Juan", "apellido": "algun apellido"}
    segundo = {"id": 2, "nombre": "Javier", "apellido": "Zepeda"}
    lista = [contenido, segundo]
    return jsonify(lista)


@app.route('/', methods=['GET'])
def saludo():
    return "Hola Enrouters"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

