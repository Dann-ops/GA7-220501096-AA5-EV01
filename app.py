from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos ficticia
usuarios = {"admin": "12345"}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data.get('usuario')
    password = data.get('password')

    if user in usuarios and usuarios[user] == password:
        return jsonify({"mensaje": "Autenticación satisfactoria"}), 200
    else:
        return jsonify({"error": "Error en la autenticación"}), 401

if __name__ == '__main__':
    app.run(debug=True)