from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>Servidor API funcionando correctamente</h1><p>Usa Postman o Curl para las pruebas de login.</p>"

# Base de datos en memoria (Diccionario)
# Estructura: {"nombre_usuario": "contraseña"}
base_datos_usuarios = {
    "profe_sena": "sena2024"  # Usuario pre-cargado para pruebas
}

# --- RUTA DE REGISTRO ---
@app.route('/registro', methods=['POST'])
def registrar_usuario():
    """
    Permite registrar un nuevo usuario en el sistema.
    Se espera un JSON con 'usuario' y 'password'.
    """
    datos = request.get_json()
    
    # Validar que lleguen los campos necesarios
    usuario = datos.get('usuario')
    password = datos.get('password')

    if not usuario or not password:
        return jsonify({"error": "Datos incompletos. Se requiere 'usuario' y 'password'"}), 400

    # Verificar si el usuario ya existe
    if usuario in base_datos_usuarios:
        return jsonify({"error": "El nombre de usuario ya se encuentra registrado"}), 409

    # Guardar el nuevo usuario
    base_datos_usuarios[usuario] = password
    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": usuario
    }), 201


# --- RUTA DE LOGIN ---
@app.route('/login', methods=['POST'])
def login():
    """
    Valida las credenciales del usuario.
    Requisito GA7-220501096-AA5-EV01
    """
    datos = request.get_json()
    usuario = datos.get('usuario')
    password = datos.get('password')

    # Lógica de autenticación
    if usuario in base_datos_usuarios and base_datos_usuarios[usuario] == password:
        # Mensaje exacto solicitado en la guía
        return jsonify({"mensaje": "Autenticación satisfactoria"}), 200
    else:
        # Mensaje de error solicitado en la guía
        return jsonify({"error": "Error en la autenticación"}), 401


# --- RUTA DE CONSULTA (OPCIONAL) ---
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    # Solo para que verifiques qué usuarios se han registrado
    return jsonify({"usuarios_registrados": list(base_datos_usuarios.keys())})

if __name__ == '__main__':
    # Lanzar el servidor en el puerto 5000
    app.run(debug=True)