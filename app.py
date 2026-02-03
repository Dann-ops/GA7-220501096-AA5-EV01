from flask import Flask, request, jsonify

# Aquí inicializo mi aplicación Flask para convertir este script en un servidor web
app = Flask(__name__)

@app.route('/')
def inicio():
    # Defino esta ruta raíz para confirmar visualmente que mi servidor está encendido
    return "<h1>Servidor API funcionando correctamente</h1><p>Usa Postman o Curl para las pruebas de login.</p>"

# Utilizo un diccionario como base de datos temporal para almacenar mis usuarios
# La clave es el nombre de usuario y el valor es la contraseña
base_datos_usuarios = {
    "profe_sena": "sena2024"  # Dejo este usuario creado para facilitar las pruebas iniciales
}

# --- RUTA DE REGISTRO ---
@app.route('/registro', methods=['POST'])
def registrar_usuario():
    """
    En esta función, recibo los datos para crear una nueva cuenta.
    Extraigo la información del cuerpo de la petición (JSON).
    """
    datos = request.get_json()
    
    # Extraigo los valores de las llaves 'usuario' y 'password'
    usuario = datos.get('usuario')
    password = datos.get('password')

    # Valido que no me envíen campos vacíos para mantener la integridad de los datos
    if not usuario or not password:
        return jsonify({"error": "Datos incompletos. Se requiere 'usuario' y 'password'"}), 400

    # Compruebo si el nombre de usuario ya existe en mi diccionario para evitar duplicados
    if usuario in base_datos_usuarios:
        return jsonify({"error": "El nombre de usuario ya se encuentra registrado"}), 409

    # Si todo está bien, guardo el nuevo usuario en mi base de datos en memoria
    base_datos_usuarios[usuario] = password
    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": usuario
    }), 201


# --- RUTA DE LOGIN ---
@app.route('/login', methods=['POST'])
def login():
    """
    Esta es la función principal de la evidencia. 
    Aquí verifico si el usuario que intenta entrar existe y tiene la clave correcta.
    """
    datos = request.get_json()
    usuario = datos.get('usuario')
    password = datos.get('password')

    # Comparo las credenciales recibidas con las que tengo almacenadas en mi diccionario
    if usuario in base_datos_usuarios and base_datos_usuarios[usuario] == password:
        # Si coinciden, devuelvo el mensaje satisfactorio requerido por la guía
        return jsonify({"mensaje": "Autenticación satisfactoria"}), 200
    else:
        # Si algo falla, devuelvo el mensaje de error solicitado
        return jsonify({"error": "Error en la autenticación"}), 401


# --- RUTA DE CONSULTA (OPCIONAL) ---
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    # He creado esta ruta adicional para poder visualizar rápidamente qué usuarios he registrado durante mis pruebas
    return jsonify({"usuarios_registrados": list(base_datos_usuarios.keys())})

if __name__ == '__main__':
    # Arranco mi servidor en modo debug para ver cambios en tiempo real durante el desarrollo
    app.run(debug=True)